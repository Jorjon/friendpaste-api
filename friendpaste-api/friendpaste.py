import requests


def fp_read(hash, json=False):
    # return data on sucess
    url = '%s/%s/raw' % (FP_URL, hash)
    try:
        r = requests.get(url)
    except requests.ConnectionError:
        return None
    return r.json() if json else r.text


def fp_write(hash, text, title="", language="text"):
    # return True on sucess
    payload = {
        "paste_snippet": text,
        "paste_language": language,
        "paste_title": title,
        "psubmit": "Save changes"
    }
    r = requests.post('%s/%s/edit' % (FP_URL, hash), data=payload)
    return r.text


def fp_create(text, title="", language="text", code=""):
    # returns new hash on success
    payload = {
        "paste_snippet": text,
        "paste_language": language,
        "paste_title": title,
        "paste_code": code,
        "paste_privacy": "open",
        "paste_password": "",
        "psubmit": "Submit post"
    }
    r = requests.post('%s/' % FP_URL, data=payload)
    return r.url.replace('%s/' % FP_URL, '')


FP_URL = 'https://friendpaste.com'