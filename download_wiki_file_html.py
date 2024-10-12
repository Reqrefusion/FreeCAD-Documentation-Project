import os
import requests
import json
import random
from datetime import datetime
from bs4 import BeautifulSoup

# API URLs
wiki_url = "https://wiki.freecad.org/api.php"
css_modules_urls = [
    "https://wiki.freecad.org/load.php?lang=tr&modules=site.styles|ext.pygments%2Ctranslate|ext.translate.edit.documentation.styles|ext.translate.tag.languages|ext.uls.pt|jquery.makeCollapsible.styles|mediawiki.ui.button%2Cicon|skins.vector.icons%2Cstyles&only=styles&skin=vector-2022",
]
js_modules_urls = [
    "https://wiki.freecad.org/load.php?lang=tr&modules=startup&only=scripts&raw=1&skin=vector-2022",
    "https://wiki.freecad.org/load.php?lang=tr&modules=ext.uls.common%2Ccompactlinks%2Cinterface%2Cpreferences%2Cwebfonts%7Cjquery%2Coojs%2Csite%7Cjquery.client%2Ccookie%2CmakeCollapsible%7Cjquery.uls.data%7Cmediawiki.String%2CTitle%2Capi%2Cbase%2Ccldr%2Ccookie%2Cexperiments%2CjqueryMsg%2Clanguage%2Cstorage%2Ctoc%2Cuser%2Cutil%7Cmediawiki.libs.pluralruleparser%7Cmediawiki.page.ready%7Cmediawiki.page.watch.ajax%7Cskins.vector.es6%2Cjs%7Cskins.vector.icons.js&skin=vector-2022&version=1xtov",
    "https://wiki.freecad.org/load.php?lang=tr&modules=ext.uls.webfonts.repository&skin=vector-2022&version=inkny",
]

# Default settings
default_config = {
    "languages": ['en'],  # Languages to be downloaded
    "download_images": False,  # Images will not be downloaded
    "last_run": None  # Last run time
}
config_path = "config.json"
output_dir = "wiki"

# Supported language codes
language_codes = [
    'bg', 'cs', 'de', 'en', 'es', 'fi', 'fr', 'hr', 'hu', 'id', 'it', 'ja',
    'ko', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'sv', 'tr', 'uk', 'vi', 'zh', 'zh-cn', 'zh-tw'
]

# Functions

def load_config():
    """Loads the configuration file or creates a new one."""
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print("Configuration file not found. Please set new configurations.")
        current_languages = default_config['languages']
        print(f"Default languages: {current_languages}")
        
        languages = input(f"If you want to add languages, please enter them separated by commas (Leave blank to use defaults): ")
        if languages:
            new_languages = languages.split(',')
            current_languages.extend(lang.strip() for lang in new_languages if lang.strip() in language_codes)
        
        download_images = input("Should images be downloaded? (y/n, Default: no): ").lower() == 'y'

        config = {
            "languages": current_languages,
            "download_images": download_images,
            "last_run": None
        }
        save_config(config)
        return config

def save_config(config):
    """Saves the configuration settings."""
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

def sanitize_name(name):
    """Cleans file names."""
    return name.replace(' ', '_').replace(':', '').replace('/', '_').strip()

def create_file_path(title):
    """Creates the correct file path based on the page title and language."""
    parts = title.split('/')
    
    # If the title has multiple parts and the last part is in language codes, check the language code
    if len(parts) > 1 and parts[-1] in language_codes:
        language_code = parts[-1]  # Last part is the language code
        content_parts = parts[:-1]  # Remaining parts are content
    else:
        language_code = None  # No language code
        content_parts = parts  # All title parts form the content

    # Create the file name
    sanitized_content = [sanitize_name(part) for part in content_parts]

    # If the language code is 'en', save directly to the wiki folder
    if language_code == "en":
        file_name = '_'.join(sanitized_content) + ".html"
        return os.path.join(output_dir, file_name)
    elif language_code:
        # If a different language code exists, save to the respective language folder
        file_name = '_'.join(sanitized_content) + ".html"
        return os.path.join(output_dir, language_code, file_name)
    else:
        # If there is no language code, save to the default folder
        file_name = '_'.join(sanitized_content) + ".html"
        return os.path.join(output_dir, file_name)


def download_css_js():
    """Downloads and saves all CSS and JS files."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Download the CSS file
    css_file = os.path.join(output_dir, "site.css")
    if not os.path.exists(css_file):
        print("Downloading and merging CSS files...")
        css_content = ""
        for url in css_modules_urls:
            css_content += requests.get(url).text + "\n"
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)
    
    # Download the JS file
    js_file = os.path.join(output_dir, "site.js")
    if not os.path.exists(js_file):
        print("Downloading and merging JS files...")
        js_content = ""
        for url in js_modules_urls:
            js_content += requests.get(url).text + "\n"
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_content)

def adjust_links(html_content, page_title, config):
    """Updates the links in the HTML content according to the local file structure."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Adjust all <a> tags' href attributes
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/File:'):
            file_name = href.split('/wiki/File:')[-1]
            a_tag['href'] = f'File/{file_name}'
        elif href.startswith('/wiki/'):
            relative_link = href.split('/wiki/')[-1]
            file_path = create_file_path(relative_link)  # Use create_file_path function to create the file path
            a_tag['href'] = file_path
        elif href.startswith('/'):
            a_tag['href'] = create_file_path(href[1:])  # Correct links starting from the root

    # Adjust all <img> tags' src attributes
    for img_tag in soup.find_all('img', src=True):
        src = img_tag['src']
        if src.startswith('/'):
            file_name = src.split('/')[-1]
            img_tag['src'] = f'File\{file_name}'

    return str(soup)

def process_page(page, config):
    """Processes and saves the content of a page."""
    page_title = page['title']
    
    # Check the page's language; if not specified in the config file, skip it
    language = page_title.split('/')[-1]
    if not any(lang == language for lang in config['languages']):
        print(f"Skipping page '{page_title}' as it is not among the selected languages.")
        return

    # Create the file path
    file_path = create_file_path(page_title)

    # Skip if the file already exists
    if os.path.exists(file_path):
        print(f"'{file_path}' already exists, skipping.")
        return

    # Fetch the page content as HTML
    print(f"Fetching content: {page_title}")
    content_params = {
        "action": "parse",
        "page": page_title,
        "prop": "text",
        "format": "json"
    }
    response = requests.get(wiki_url, params=content_params)
    
    if response.status_code != 200:
        print(f"Error: Could not download {page_title}. HTTP Code: {response.status_code}")
        return
    
    data = response.json()
    html_content = data.get('parse', {}).get('text', {}).get('*', '')

    if not html_content:
        print(f"Content for '{page_title}' is empty, skipping.")
        return

    # Add CSS and JS files to the HTML
    css_link = f'<link rel="stylesheet" type="text/css" href="site.css">\n'
    js_script = f'<script src="site.js"></script>\n'
    full_html = f"{css_link}{html_content}{js_script}"

    # Correct links
    full_html = adjust_links(full_html, page_title, config)

    # Save the HTML file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"Successfully saved '{page_title}': {file_path}")

def main():
    """Main function."""
    config = load_config()
    download_css_js()

    # Fetch pages from all_pages.json
    if not os.path.exists("all_pages.json"):
        print("all_pages.json file not found!")
        return

    with open("all_pages.json", 'r', encoding='utf-8') as f:
        all_pages = json.load(f)

    random.shuffle(all_pages)

    # Process each page
    for page in all_pages:
        process_page(page, config)

    # Update the last run time
    config['last_run'] = datetime.utcnow().isoformat()
    save_config(config)

if __name__ == "__main__":
    main()
