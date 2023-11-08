#!/usr/bin/python3
"""sumary_line
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """sumary_line
    """

    url = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Custom)'}
    response = requests.get(url, headers=headers, params={"after": after})

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
