import requests


def j(u):
    r = requests.get(u)
    if r.status_code == 200:
        return r.json()
    else:
        return {}
