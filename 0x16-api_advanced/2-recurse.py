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
    params = {
            "limit": 100,
            "after": after,
            "count": count
    }
    response = get(url_base, params=params,
                   headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return None
    res = response.json().get("data")
    count += res.get("dist")
    after = res.get("after")
    for child in res.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
