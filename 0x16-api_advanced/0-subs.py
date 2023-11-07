#!/usr/bin/python3
"""function that queries the Reddit API"""
from requests import get


def number_of_subscribers(subreddit):
    """ function that queries Reddit API and returns number of subs """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \Gecko/20100101 Firefox/108.0"
    }
    resp = get(link, head=head).json()
    subs = resp.get('data', {}).get('subscribers', 0)
    return subs
