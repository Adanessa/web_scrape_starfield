from bs4 import BeautifulSoup
import requests
import re

def find_api_endpoints(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <script> tags
    script_tags = soup.find_all('script')

    # Look for patterns that resemble API endpoints in the script content
    api_endpoints = []
    for script in script_tags:
        script_content = script.get_text()
        # Use regular expressions to find potential API endpoints
        matches = re.findall(r'(https?://\S+)', script_content)
        api_endpoints.extend(matches)

    return api_endpoints

url = "https://starfieldwiki.net/wiki/Starfield:Planets"
api_endpoints = find_api_endpoints(url)

if api_endpoints:
    print("API endpoints found:")
    for endpoint in api_endpoints:
        print(endpoint)
else:
    print("No API endpoints found.")
