import requests

API_URL = "https://friendpaste.com/"


def post_text(title: str, text: str, hash: str):
    data = {"paste_title": title, "paste_snippet": text, "paste_language": "text", "psubmit": "Save+changes"}
    headers = {}
    r = requests.post(API_URL + hash + '/edit', data=data, headers=headers)
    return r
