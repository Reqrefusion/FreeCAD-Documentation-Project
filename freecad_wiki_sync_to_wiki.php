<?php

require_once('botclasses.php');

date_default_timezone_set('UTC');  // Set timezone to UTC

$githubRepoPath = "Reqrefusion/FreeCAD-Documentation-Project";

$githubToken = "ghp_XXX";

$wikiUsername = 'XXX';

$wikiPassword = 'XXX';

$apiUrl = 'https://wiki.freecad.org/api.php';

$webhookSecret = "XXX";

$languageCodes = array(
    'bg', 'cs', 'de', 'en', 'es', 'fi', 'fr', 'hr', 'hu', 'id', 'it', 'ja',
    'ko', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'sv', 'tr', 'uk', 'vi', 'zh', 'zh-cn', 'zh-tw', 'zh-hant'
);

// Function to retrieve file content from GitHub repository
function getGithubFileContent($filePath) {
    global $githubRepoPath, $githubToken;
    $githubApiUrl = "https://api.github.com/repos/$githubRepoPath/contents/" . $filePath;
    $ch = curl_init($githubApiUrl);

    // Set authorization and user-agent headers
    $headers = array(
        'Authorization: token ' . $githubToken,
        'User-Agent: PHP'
    );

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $response = curl_exec($ch);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    curl_close($ch);

    // Decode response if successful
    if ($httpcode == 200) {
        $content = json_decode($response, true);
        return array(
            'content' => base64_decode($content['content']), // Decode base64 content
            'sha' => $content['sha'], // Get file SHA
            'lastModified' => new DateTime($content['commit']['committer']['date']) // Get last modified date
        );
    } else {
        return null;
    }
}

// Function to reverse file path for Wiki format
function reverseFilePath($filePath) {
    global $languageCodes;

    // Remove 'wiki/' prefix from the file path
    $filePath = str_replace('wiki/', '', $filePath);
    $parts = explode('/', $filePath);

    // Check for language code in the path
    $languageCode = null;
    if (in_array($parts[0], $languageCodes)) {
        $languageCode = array_shift($parts);  // Remove and save language code
    }

    // Get file name, removing ".wikitext" and replacing characters
    $fileName = str_replace('.wikitext', '', array_pop($parts));
    $fileName = str_replace('_', ' ', $fileName);
    $fileName = str_replace(';', ':', $fileName);

    // Append language code to file name if available
    if ($languageCode) {
        $fileName .= '/' . $languageCode;
    }

    // Rebuild path if there are remaining parts
    if (!empty($parts)) {
        $fileName = implode('/', $parts) . '/' . $fileName;
    }

    return $fileName;
}

$payload = file_get_contents('php://input');
$signature = 'sha256=' . hash_hmac('sha256', $payload, $webhookSecret);
$headers = getallheaders();
if (!isset($headers['X-Hub-Signature-256']) || !hash_equals($signature, $headers['X-Hub-Signature-256'])) {
    http_response_code(403);
    exit('Invalid webhook signature');
}

$data = json_decode($payload, true);

if (!empty($data['commits'])) {
    foreach ($data['commits'] as $commit) {

        // Check if the author email is valid
        if (!str_ends_with($commit['author']['email'], '@users.noreply.github.com')) {
            echo "No action taken: Author email is invalid ({$commit['author']['email']}).\n";
            continue;
        }

        $authorUserName = $commit['author']['username'];
        $commitMessage = $commit['message'];
        $shortCommitId = substr($commit['id'], 0, 7);

        // Process both added and modified files together
        $filesToProcess = array_merge($commit['added'], $commit['modified']);

        foreach ($filesToProcess as $filePath) {
            // Skip files outside the 'wiki/' directory
            if (strpos($filePath, "wiki/") !== 0) {
                continue;
            }

            // Retrieve the file content from GitHub
            $githubFile = getGithubFileContent($filePath);

            if ($githubFile) {
                $wikiTitle = reverseFilePath($filePath);
                echo "Updated Wiki Title: $wikiTitle\n";
                echo "Author: $authorUserName\n";
                echo "Commit Message: $commitMessage\n";

                $bot = new wikipedia($apiUrl, $wikiUsername, $wikiPassword);
                if ($bot->login($wikiUsername, $wikiPassword)) {
                    echo "Successfully logged in.\n";
                    $wikiContent = $bot->getpage($wikiTitle);

                    // Skip files that start with "wiki/File/"
                    if (strpos($filePath, "wiki/File/") === 0) {
                        echo "Changes to files are currently not supported.\n";
                        continue;
                    }
					
                    // Check if the content has changed
                    if (trim($wikiContent) != trim($githubFile['content'])) {
                        $editToken = $bot->getedittoken($wikiTitle);
                        if (!$editToken) {
                            echo "ERROR: Failed to retrieve edit token.\n";
                            continue;
                        }

                        $summary = "$shortCommitId $commitMessage (Author: $authorUserName)";
                        $editResult = $bot->edit($wikiTitle, $githubFile['content'], $summary, $editToken);

                        if ($editResult['edit']['result'] === 'Success') {
                            echo "$wikiTitle successfully updated.\n";
                        } else {
                            echo "$wikiTitle update failed.\n";
                            print_r($editResult);
                        }
                    } else {
                        echo "$wikiTitle is already up-to-date.\n";
                    }
                } else {
                    echo "Login failed.\n";
                }
            } else {
                echo "Failed to retrieve GitHub file content: $filePath\n";
            }
        }
    }
} else {
    echo "No files found in the commit.\n";
}
?>
