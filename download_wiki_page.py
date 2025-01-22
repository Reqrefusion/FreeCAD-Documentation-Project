import os
import requests
import json
import random

# FreeCAD wiki API URL and parameters
url = "https://wiki.freecad.org/api.php"
content_params = {
    "action": "query",
    "prop": "revisions",
    "rvprop": "content",
    "format": "json"
}

# Load and shuffle all pages
with open('all_pages.json', 'r', encoding='utf-8') as f:
    all_pages = json.load(f)
random.shuffle(all_pages)

# Supported languages
language_codes = [
    'bg', 'cs', 'de', 'en', 'es', 'fi', 'fr', 'hr', 'hu', 'id', 'it', 'ja',
    'ko', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'sv', 'tr', 'uk', 'vi', 'zh', 'zh-cn', 'zh-tw'
]
output_dir = "wiki"

# Function to sanitize file names
def sanitize_name(name):
    return name.replace(' ', '_').replace(':', ';').strip()

# Function to create the file path based on the page title
def create_file_path(title):
    parts = title.split('/')
    last_part = parts[-1]
    
    # Check for language code
    language_code = next((lang for lang in language_codes if lang in last_part), None)
    content_parts = parts[:-1] if language_code else parts

    # Build file name and path
    sanitized_content = [sanitize_name(part) for part in content_parts]
    file_name = os.path.join(language_code or '', *sanitized_content) + ".wikitext"
    return os.path.join(output_dir, file_name)

# Process and save pages
for page in all_pages:
    page_title = page['title']
    file_path = create_file_path(page_title)

    # Skip if the file already exists
    if os.path.exists(file_path):
        print(f"'{file_path}' already exists, skipping.")
        continue

    # Fetch the page content from the API
    print(f"Fetching content for: {page_title}")
    content_params['titles'] = page_title
    response = requests.get(url, params=content_params)
    
    if response.status_code != 200:
        print(f"Error: Failed to fetch {page_title}. HTTP Code: {response.status_code}")
        continue

    data = response.json()
    pages = data['query']['pages']
    page_id = next(iter(pages))
    
    if 'revisions' in pages[page_id]:
        page_content = pages[page_id]['revisions'][0]['*']

        # Create directories and save the content
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"'{page_title}' successfully saved to: {file_path}")
    else:
        print(f"'{page_title}' has no content, skipping.")
