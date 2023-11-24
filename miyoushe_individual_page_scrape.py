import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def extract_image_links(url):

    # Use a headless browser
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')

    # Create a new instance of the Firefox driver with headless mode
    driver = webdriver.Firefox(options=options)

    # Set a maximum wait time for elements (in seconds)
    wait = WebDriverWait(driver, 60)

    try:
        # Load the webpage
        driver.get(url)

        # Wait until the content element is present
        content_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'mhy-article-page__content')))

        # Find all elements with class 'ql-image-box' under 'mhy-article-page__content'
        image_boxes = content_element.find_elements(By.CLASS_NAME, 'ql-image-box')

        # Extract and return the link with the large image for each 'ql-image-box'
        image_links = [box.find_element(By.CSS_SELECTOR, 'img').get_attribute('large') for box in image_boxes]
    
    except (TimeoutException, WebDriverException) as e:
        print(f"Failed to access the page {url}: {e}")
        image_links = None

    finally:
        # Close the browser
        driver.quit()

    return image_links

# Load the JSON file
with open("insert_json_to_read_path_here", 'r', encoding='utf-8') as file:
    entries = json.load(file)

failed_entries = []

# Process each entry
for entry in entries:
    # Extract image links using the provided function
    print("Extracting:", entry['name'], entry['post_date'], entry['url'])
    image_links = extract_image_links(entry['url'])

    if image_links is not None:
        # Add the 'images' key to the entry
        entry['images'] = [{"image": link} for link in image_links]
        print("Extracted!")
    else:
        # If timed out, add the entry to the failed list
        failed_entries.append(entry)
        print("Failed!")

# Save the updated JSON to a new file
with open('insert_json_path_here', 'w', encoding='utf-8') as output_file:
    json.dump({"listingValue": len(entries), "listings": entries}, output_file, ensure_ascii=False, indent=2)

# Save the failed entries to a separate JSON file
with open('insert_json_path_here', 'w', encoding='utf-8') as failed_file:
    json.dump({"listingValue": len(failed_entries), "listings": failed_entries}, failed_file, ensure_ascii=False, indent=2)
