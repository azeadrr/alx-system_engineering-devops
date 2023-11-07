#!/usr/bin/python3
"""function that queries the Reddit API"""
from requests import get


def number_of_subscribers(subscritionreddit):
    """ function that queries the Reddit API and returns the number of subscribers """
    if subscritionreddit is None or not isinstance(subscritionreddit, str):
        return 0
    link = "https://www.reddit.com/r/{}/about.json".format(subscritionreddit)
    head = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \Gecko/20100101 Firefox/108.0"
    }
    resp = get(link, head=head).json()
    subs = resp.get('data', {}).get('subscribers', 0)
    return subs
