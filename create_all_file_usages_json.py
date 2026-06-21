# ... (truncated) ...
    "list": "allfileusages",  # Get all file usages
    "afunique": "",  # Retrieve unique file usages
    "aflimit": "max",  # Get the maximum number of results per request
    "format": "json"  # Output in JSON format
}

all_file_usages = []  # Store all file usages here
next_request_params = {}  # Store the API's continuation parameters (see https://www.mediawiki.org/wiki/API:Continue)
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
        print("Refer to https://www.mediawiki.org/wiki/API:Errors_and_warnings for troubleshooting")
        break
# ... (truncated) ...