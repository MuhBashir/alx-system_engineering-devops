#!/usr/bin/python3

"""
Script that prints the titles of the first 10 hot posts 
listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 114.0.5735.90 '}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    res = get(url, headers=user_agent, params=params)
    results = res.json()

    try:
        my_data = results['data'].get('children')

        for i in my_data:
            print(i['data'].get('title'))

    except Exception:
        print("None")
