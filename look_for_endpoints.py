import json

# Load the existing JSON data
with open('existing_data.json', 'r') as json_file:
    existing_data = json.load(json_file)

# Define the list of keys to add
keys_to_add = ["type", "Gravity", "Temperature", "Atmosphere", "Magnetosphere", "Water", "Biomes", "Traits", "Fauna", "Flora", "Resources", "Domesticable", "Gatherable", "Hab_rank", "Days"]

# Iterate over each system and planet
for system_name, planets in existing_data.items():
    for planet_name, data in planets.items():
        # Iterate over each key to add
        for key in keys_to_add:
            # Check if the key is missing
            if key not in data:
                # Add the key with an empty list
                data[key] = []

# Save the updated data to a new file
with open('updated_data.json', 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)

print("Keys added to existing data.")

















































# from bs4 import BeautifulSoup
# import requests
# import re

# def find_api_endpoints(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all <script> tags
#     script_tags = soup.find_all('script')

#     # Look for patterns that resemble API endpoints in the script content
#     api_endpoints = []
#     for script in script_tags:
#         script_content = script.get_text()
#         # Use regular expressions to find potential API endpoints
#         matches = re.findall(r'(https?://\S+)', script_content)
#         api_endpoints.extend(matches)

#     return api_endpoints

# url = "https://starfieldwiki.net/wiki/Starfield:Planets"
# api_endpoints = find_api_endpoints(url)

# if api_endpoints:
#     print("API endpoints found:")
#     for endpoint in api_endpoints:
#         print(endpoint)
# else:
#     print("No API endpoints found.")
