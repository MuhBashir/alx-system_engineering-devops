#!/usr/bin/python3
"""
Get number of subscribers for the subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
     function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. 
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = get(url, headers=user_agent)
    results = res.json()

    try:
        return results["data"].get('subscribers')

    except Exception:
        return 0
