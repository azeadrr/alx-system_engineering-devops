#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0 (by /u/azeadrr)'}
    params = {
            "limit": 10
            }
    response = get(url, params=params, headers=headers,
                   allow_redirects=False).json()
    children = response.get("data", {}).get("children", None)
    if children:
        for subject in children:
            print(subject.get("data").get("title"))
    else:
        print("None")
