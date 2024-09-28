import os
import requests
import json
import random

# Load and shuffle the list of file usages
with open('all_file_usages.json', 'r', encoding='utf-8') as f:
    all_file_usages = json.load(f)
random.shuffle(all_file_usages)

# Directory to save downloaded files
output_dir = "wiki\File"
os.makedirs(output_dir, exist_ok=True)

# Base URL for FreeCAD wiki file downloads
base_url = 'https://wiki.freecadweb.org/Special:FilePath/'

# Function to sanitize file names
def sanitize_name(name):
    return name.replace(' ', '_').replace(':', ';').strip()

# Function to create the file path based on the file title
def create_file_path(file_title):
    # Remove "File:" from the title and sanitize the file name
    sanitized_file_name = sanitize_name(file_title)
    return os.path.join(output_dir, sanitized_file_name)

# Function to download files
def download_file(file_info):
    file_title = file_info.get('title')
    file_path = create_file_path(file_title.replace('File:', ''))

    # Skip if the file already exists
    if os.path.exists(file_path):
        print(f"'{file_path}' already exists, skipping.")
        return

    # Build the download URL
    clean_title = file_title.replace('File:', '').replace(' ', '_').replace(':', ';')
    url = base_url + clean_title

    # Download the file
    try:
        print(f"Downloading: {url}")
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"'{file_title}' successfully saved to: {file_path}")
        else:
            print(f"Failed to download {file_title}. HTTP Code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while downloading {file_title}: {e}")

# Iterate over the shuffled list of files and download them
for file_info in all_file_usages:
    download_file(file_info)
