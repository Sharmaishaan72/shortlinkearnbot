import requests
import os

def create_shortlink(url):
    shortlink_api_url = os.getenv("shortlink_api")
    api_token = os.getenv("shortlink_token")
    shortlink_api_url = shortlink_api_url.replace("{token}",api_token).replace("{url}",url)
    response = requests.get(shortlink_api_url)
    return response.json()[os.getenv("json_key")]

def createmainlink(linkid):
    url = f"{os.getenv('ngrok_url')}{os.getenv('path_shortlink')}/{linkid}"
    shortlink = create_shortlink(url)
    return shortlink
