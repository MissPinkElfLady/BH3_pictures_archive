import json

# used to see if there are anything that is left out by the scraper

# Open the file in read mode
with open('insert_your_json_path_here', 'r',encoding='utf-8') as file:
    # Load JSON data from the file with decoding Unicode escape sequences
    json_data = json.load(file)

# Collect names with "壁纸" and no images
selected_entries = [
    {"name": item["name"], "post_date": item["post_date"], "url": item["url"]}
    for item in json_data.get("listings", [])
    if "name" in item and ("壁纸" in item.get("name", "") or "壁纸" in item.get("name", "").lower())
    and "images" not in item
]

# Save the selected entries as a new JSON file
with open('selected_entries.json', 'w', encoding='utf-8') as output_file:
    json.dump(selected_entries, output_file, ensure_ascii=False, indent=2)

print(selected_entries)
