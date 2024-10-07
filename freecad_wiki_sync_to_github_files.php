<?php
date_default_timezone_set('UTC');  // Set timezone to UTC

$githubRepoPath = "Reqrefusion/FreeCAD-Documentation-Project";  // GitHub repository path

$githubToken = "ghp_XXX"; // Place your GitHub API token here.

$invalidPrefixes = array('Translations:', 'Draft:', 'Help:');  // Remove 'File:' and 'Images:' from here

// Function to get the file content from GitHub
function getGithubFileContent($filePath) {
    global $githubRepoPath, $githubToken;
    $githubApiUrl = "https://api.github.com/repos/$githubRepoPath/contents/" . $filePath;
    $ch = curl_init($githubApiUrl);

    $headers = array(
        'Authorization: token ' . $githubToken,
        'User-Agent: PHP'
    );

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $response = curl_exec($ch);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    curl_close($ch);

    if ($httpcode == 200) {
        $content = json_decode($response, true);
        return array(
            'content' => base64_decode($content['content']),  // Decode the Base64 content
            'sha' => $content['sha'],  // Store the SHA value for updates
            'lastModified' => new DateTime($content['commit']['committer']['date'])  // Last modified date
        );
    } else {
        return null;
    }
}

// Function to update or create a file on GitHub
function updateGithubFile($filePath, $newContent, $sha, $pageTitle, $user, $comment) {
    global $githubRepoPath, $githubToken;
    $githubApiUrl = "https://api.github.com/repos/$githubRepoPath/contents/" . $filePath;

    $commitMessage = $comment ?: "Updated file $pageTitle";  // Default commit message if no comment

    // FreeCAD Wiki message board URL for the user
    $wikiUserUrl = "https://wiki.freecad.org/User:" . urlencode($user);

    // Author information for the commit
    $authorData = array(
        "name" => $user,  // FreeCAD Wiki username
        "email" => $wikiUserUrl  // Message board URL instead of email
    );

    // Data to send to GitHub API
    $data = array(
        "message" => $commitMessage,
        "content" => base64_encode($newContent),  // Encode the content in Base64
        "sha" => $sha,  // SHA of the previous file
        "author" => $authorData  // Author information
    );

    // Send the request via cURL
    $ch = curl_init($githubApiUrl);

    $headers = array(
        'Authorization: token ' . $githubToken,
        'User-Agent: PHP',
        'Content-Type: application/json'
    );

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

    $response = curl_exec($ch);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $responseData = json_decode($response, true);

    curl_close($ch);

    if ($httpcode == 200 || $httpcode == 201) {  // 200 for update, 201 for create
        echo "SUCCESS: '$filePath' successfully updated/created on GitHub by $user.<br>";
        return true;
    } else {
        echo "ERROR: Failed to update '$filePath' on GitHub. HTTP Code: $httpcode. Message: " . $responseData['message'] . "<br>";
        return false;
    }
}

// Function to download the image file from the Wiki and return binary data
function downloadWikiFile($fileTitle) {
    $fileUrl = "https://wiki.freecad.org/Special:FilePath/" . str_replace(' ', '_',$fileTitle);  // Direct URL to file
    echo "INFO: Trying to download file from: $fileUrl<br>";  // Debugging output

    $ch = curl_init($fileUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);  // Follow redirects

    $fileContent = curl_exec($ch);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    curl_close($ch);

    if ($httpcode == 200) {
        return $fileContent;
    } else {
        echo "ERROR: Could not download file '$fileTitle'. HTTP Code: $httpcode<br>";
        return null;
    }
}


// Function to create a valid file path based on the file name (calls sanitize_name)
function createFilePath($fileTitle) {
    return "wiki/File/" . sanitize_name($fileTitle);
}

// Function to sanitize file names (removes "File:" or "Images:" and replaces invalid characters)
function sanitize_name($name) {
    // First, remove the "File:" or "Images:" prefix using str_replace
    $name = str_replace(array('File:', 'Images:'), '', $name);
    
    // Replace invalid characters (spaces and colons)
    return str_replace(array(' ', ':'), array('_', ';'), $name);  // Replace invalid characters
}

// Check for recent changes made in the last 20 minutes
$currentTime = new DateTime();  // Get the current time
$timeLimit = clone $currentTime;
$timeLimit->modify('-20 minutes');  // Go back 20 minutes

// Format the timestamp
$timestampStart = $timeLimit->format('Y-m-d\TH:i:s\Z');  // 20 minutes ago timestamp

$wikiRecentChangesUrl = "https://wiki.freecad.org/api.php?action=query&list=recentchanges&rcprop=title|timestamp|user|comment&rclimit=500&rcend=" . $timestampStart . "&format=json";

// Fetch the recent changes from the Wiki API
$recentChanges = file_get_contents($wikiRecentChangesUrl);
$recentChanges = json_decode($recentChanges, true);

// If there are no errors, process the changes
if (isset($recentChanges['query']['recentchanges'])) {
    $recentPages = array_reverse($recentChanges['query']['recentchanges']);  // Sort changes from oldest to newest

    foreach ($recentPages as $page) {
        $pageTitle = $page['title'];
        $user = $page['user'];  // User who made the change
        $comment = $page['comment'];  // Comment on the change
        $timestamp = new DateTime($page['timestamp']);  // Time of the change

        // Check if the page is a file or image
        if (strpos($pageTitle, 'File:') === 0 || strpos($pageTitle, 'Images:') === 0) {
            echo "Processing file or image: $pageTitle (Modified by: $user, Comment: '$comment')<br>";

            // Generate the GitHub file path
            $filePath = createFilePath($pageTitle);

            // Get the existing file content and last modified date from GitHub
            $existingFileData = getGithubFileContent($filePath);

            // Compare modification times to decide if the file needs to be updated
            if ($existingFileData && $existingFileData['lastModified'] >= $timestamp) {
                echo "INFO: '$filePath' is already up-to-date.<br>";
                continue;  // If the GitHub file is up-to-date, skip
            }

            // Download the file from the Wiki
            $fileContent = downloadWikiFile($pageTitle);
            if ($fileContent !== null) {
                // Update the file if it exists, or create a new one
                if ($existingFileData) {
                    echo "INFO: Updating existing file '$filePath' on GitHub...<br>";
                    updateGithubFile($filePath, $fileContent, $existingFileData['sha'], $pageTitle, $user, $comment);
                } else {
                    echo "INFO: Creating new file '$filePath' on GitHub...<br>";
                    updateGithubFile($filePath, $fileContent, null, $pageTitle, $user, $comment);
                }
            }
        } else {
            echo "INFO: '$pageTitle' is not a file or image, skipping.<br>";
        }
    }
} else {
    echo "ERROR: Could not fetch recent changes from the wiki.<br>";
}

echo "All changes processed.<br>";

?>
