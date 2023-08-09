#!/usr/bin/python3
"""
query Reddit API and hot (top 10) posts of a subreddit.
"""
import requests


def top_ten(subreddit):
    """ get hots

    Args:
        subreddit(str): subreddit name
    """

    if subreddit is None or type(subreddit) is not str:
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'alx-devops-0x16 - maradeben'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        resp_json = resp.json()
        children = resp_json.get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
    else:
        print(None)
