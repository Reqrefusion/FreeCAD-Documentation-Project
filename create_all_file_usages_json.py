import requests
import json

# FreeCAD Wiki API URL
api_url = "https://wiki.freecad.org/api.php"

# Define API parameters
params = {
    "action": "query",
    "list": "allfileusages",  # Get all file usages
    "afunique": "",  # Retrieve unique file usages
    "aflimit": "max",  # Get the maximum number of results per request
    "format": "json"  # Output in JSON format
}

all_file_usages = []  # Store all file usages here
next_request_params = {}  # Store the API's continuation parameters
total_files = 0  # Track the total number of files retrieved

# Keep making requests until all file usages are retrieved
while True:
    # Send request to the API
    print(f"Sending request to the API... (Total files retrieved so far: {total_files})")
    response = requests.get(api_url, params={**params, **next_request_params})
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
    else:
        print(f"Request failed! HTTP Status Code: {response.status_code}")
        break

    # Parse the JSON response
    data = response.json()

    # Accumulate the file usages retrieved
    file_usages_in_response = len(data['query']['allfileusages'])
    all_file_usages.extend(data['query']['allfileusages'])
    total_files += file_usages_in_response

    # Provide feedback on the number of file usages retrieved
    print(f"{file_usages_in_response} file usages retrieved. Total files so far: {total_files}")

    # Check if the API has a "continue" parameter to get more data
    if 'continue' in data:
        next_request_params = data['continue']
        print(f"Continue parameter found: {next_request_params}. Preparing the next request...\n")
    else:
        print("All file usages have been retrieved!")
        break  # Exit the loop if there are no more file usages

# Save the result to a JSON file
with open('all_file_usages.json', 'w', encoding='utf-8') as f:
    json.dump(all_file_usages, f, ensure_ascii=False, indent=4)

print(f"\nAll file usages successfully saved to 'all_file_usages.json'.")
print(f"Total number of file usages retrieved: {total_files}")
