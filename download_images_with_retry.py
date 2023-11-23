import os
import requests
from urllib.parse import urlparse
from datetime import datetime
import json
from requests.exceptions import ChunkedEncodingError, RequestException

MAX_RETRIES = 5

def download_image(url, folder_path, filename):
    response = requests.get(url, timeout=(10, 30))
    response.raise_for_status()
    
    # Save the image
    with open(os.path.join(folder_path, filename), 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {url}")

def download_image_with_retry(url, folder_path, filename, failed_attempts):
    for attempt in range(MAX_RETRIES):
        try:
            download_image(url, folder_path, filename)
            break  # Break the loop if successful
        except (ChunkedEncodingError, RequestException) as e:
            print(f"Error downloading {url}: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying... Attempt {attempt + 2}/{MAX_RETRIES}")
            else:
                print(f"All attempts failed. Adding to failed attempts.")
                failed_attempts.append({'url': url, 'filename': filename, 'error': str(e)})

def download_images_from_json(json_data, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    failed_attempts = []

    for listing in json_data.get('listings', []):
        post_date = listing.get('post_date')
        name = listing.get('name')
        images = listing.get('images', [])
        
        for index, image_info in enumerate(images, start=1):
            image_url = image_info.get('image')
            if image_url:
                # Extract the file extension from the URL
                file_extension = os.path.splitext(urlparse(image_url).path)[1]
                # Generate the filename based on post_date, name, and index
                filename = f"{post_date}_{name}_image_{index}{file_extension}"
                # Download the image with retries and track failed attempts
                download_image_with_retry(image_url, download_folder, filename, failed_attempts)

    return failed_attempts

if __name__ == "__main__":
    # Replace 'your_json_file.json' with the actual path to your JSON file
    json_file_path = "C:/Users/awake/Desktop/Mihoyo_scrape/run_results_stigmata_copy.json"

    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    download_folder = 'C:/Users/awake/Desktop/Mihoyo_scrape/Stigmata'
    failed_attempts = download_images_from_json(json_data, download_folder)

    # Print or process failed attempts
    if failed_attempts:
        print("\nFailed Attempts:")
        for attempt in failed_attempts:
            print(f"URL: {attempt['url']}, Filename: {attempt['filename']}, Error: {attempt['error']}")
    else:
        print("\nAll images downloaded successfully.")
