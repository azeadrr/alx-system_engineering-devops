#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests import get


def recurse(subreddit, hot_list=[], after=""):
    """function that queries the Reddit API"""

    url_base = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Custom)'}
    resp = requests.get(url_base, headers=headers, params={"after": after})

    if resp.status_code == 200:
        data = resp.json()
        for pst in data['data']['children']:
            hot_list.append(pst['data']['title'])
        after = data['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
