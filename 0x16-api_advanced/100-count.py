#!/usr/bin/python3
"""function that queries the Reddit API"""
import json
from requests import get


def count_words(subreddit, word_list, after="", count=[]):
    """function that queries the Reddit API"""
    if after == "":
        count = [0] * len(word_list)

    url_base = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    headers = {"user-agent": 'bhalut'}
    req = get(url_base, params=params,
              allow_redirects=False, headers=headers)
    if req.status_code == 200:
        data = req.json()

        for tpc in (data['data']['children']):
            for word in tpc['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            lst = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        lst.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        x = count[i]
                        count[i] = count[j]
                        count[j] = x
                        x = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = x

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in lst:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)
