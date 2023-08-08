#!/usr/bin/python3
"""
query Reddit API and hot (top 10) posts of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ get subreddit subscribers

    Args:
        subreddit(str): subreddit name
    """

    if subreddit is None or type(subreddit) is not str:
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alx-devops-0x16 - maradeben'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 404:
        return (None)

    resp_json = resp.json().get('data')
    after = resp_json.get("after")
    count += resp_json.get("dist")
    children = resp_json.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return (hot_list)
