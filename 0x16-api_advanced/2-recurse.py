#!/usr/bin/python3
"""function that queries the Reddit API"""
from requests import get


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    function that queries the Reddit API
    """

    url_base = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    response = requests.get(url_base, headers=headers, params={"after": after})

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
