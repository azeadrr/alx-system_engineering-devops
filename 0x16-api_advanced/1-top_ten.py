#!/usr/bin/python3
"""function that queries the Reddit API"""
from requests import get


def top_ten(subreddit):
    """prints titles of first 10 hot posts"""
    
    url_base = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0 (by /u/bouhvli)'}

    resp = requests.get(url_base, headers=headers)
    if resp.status_code == 200:
        try:
            dt = resp.json()
            posts = dt['data']['children']
            for i, post in enumerate(posts):
                title = post['data']['title']
                print("{}. {}".format(i + 1 - 1, title))
        except(KeyError):
            print("None")
    else:
        print("None")
