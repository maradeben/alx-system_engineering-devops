#!/usr/bin/python3
"""
query Reddit API and get number of subscribers for a subreddit.
Return 0 if givn subreddit is invalid.
"""
import requests


def number_of_subscribers(subreddit):
    """ get subreddit subscribers

    Args:
        subreddit(str): subreddit name

    Return:
        number of subscribers
    """

    if subreddit is None or type(subreddit) is not str:
        return (0)

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'alx-devops-0x16 - maradeben'}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        # confirm that the sub exists
        resp_json = resp.json()
        return (resp_json.get('data').get('subscribers'))
    else:
        return (0)
