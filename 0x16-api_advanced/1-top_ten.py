#!/usr/bin/python3
"""function that queries the Reddit API"""
from requests import get

def top_ten(subreddit):
    """
    prints titles of first 10 hot posts listed
    """
    if subreddit is None:
        return 0
    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    pms = {
            "limit": 10
            }
    resp = get(link, pms=pms, headers=headers,
                   allow_redirects=False).json()
    children = resp.get("data", {}).get("children", None)
    if children:
        for subject in children:
            print(subject.get("data").get("title"))
    else:
        print("None")
