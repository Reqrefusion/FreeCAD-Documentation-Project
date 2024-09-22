import requests
import json

# Define the API URL
url = "https://wiki.freecad.org/api.php"

# Set API parameters
params = {
    "action": "query",
    "list": "allpages",
    "aplimit": "max",  # Get the maximum number of pages
    "format": "json"
}

all_pages = []  # Store all pages here
continue_param = {}  # Store the API's continue parameter
page_count = 0  # Track the total number of pages retrieved

while True:
    # Send request to the API
    print(f"Sending request to the API... (Total pages retrieved so far: {page_count})")
    response = requests.get(url, params={**params, **continue_param})
    
    # Check the request status
    if response.status_code == 200:
        print("Request successful!")
    else:
        print(f"Request failed! HTTP Code: {response.status_code}")
        break

    data = response.json()

    # Accumulate the pages retrieved
    page_count_in_response = len(data['query']['allpages'])
    all_pages.extend(data['query']['allpages'])
    page_count += page_count_in_response

    # Provide feedback on the number of pages retrieved
    print(f"{page_count_in_response} pages retrieved. Total pages so far: {page_count}")

    # Check if the API has a "continue" parameter to get more pages
    if 'continue' in data:
        continue_param = data['continue']
        print(f"Continue parameter found: {continue_param}. Preparing the next request...\n")
    else:
        print("All pages have been retrieved!")
        break  # Exit the loop if there is no more data

# Save the result to a JSON file
with open('all_pages.json', 'w', encoding='utf-8') as f:
    json.dump(all_pages, f, ensure_ascii=False, indent=4)

print(f"\nAll pages successfully saved to 'all_pages.json'.")
print(f"Total number of pages retrieved: {page_count}")
