import requests
import re

def fetch_url(url):
    response = requests.get(url)
    return response.text

def find_js_code(html_content):
    js_code_blocks = re.findall(r'<script\b[^>]*>(.*?)</script>', html_content, flags=re.DOTALL)
    return js_code_blocks

def find_api_endpoints(js_code_blocks):
    api_endpoints = []
    for block in js_code_blocks:
        if 'fetch' in block or 'XMLHttpRequest' in block:
            api_endpoints.extend(re.findall(r'https?://\S+', block))
    return api_endpoints

def main():
    urls = ['https://example.com/page1', 'https://example.com/page2']
    for url in urls:
        html_content = fetch_url(url)
        js_code_blocks = find_js_code(html_content)
        api_endpoints = find_api_endpoints(js_code_blocks)
        if api_endpoints:
            print(f'API endpoints found for {url}:')
            for endpoint in api_endpoints:
                print(endpoint)

if __name__ == "__main__":
    main()
