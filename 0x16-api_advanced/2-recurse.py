#!/usr/bin/python3
"""
query Reddit API recursively for list of hots
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ get recursively

    Args:
        subreddit(str): subreddit name
        hot_list(list): [] list to hold hot topics
        after(str): "" to hold the after parameter
        count(int): 0 of topics found
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

    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
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
