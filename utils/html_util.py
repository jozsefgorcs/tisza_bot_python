import requests

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None