#!/usr/bin/python3
"""function that queries the Reddit API"""
from requests import get

def top_ten(subreddit):
    """
    prints titles of first 10 hot posts listed
    """
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    params = {
            "limit": 10
            }
    resp = get(url, params=params, headers=headers,
                   allow_redirects=False).json()
    child = resp.get("data", {}).get("child", None)
    if child:
        for subject in child:
            print(subject.get("data").get("title"))
    else:
        print("None")
