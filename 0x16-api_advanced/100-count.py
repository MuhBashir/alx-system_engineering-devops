#!/usr/bin/python3
"""queries the Reddit API, parses the title of all 
hot articles, and prints a sorted count of given 
keywords (case-insensitive, delimited by spaces. 
Javascript should count as javascript, but java 
should not)."""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """getting the numbers of words"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        word = count[i]
                        count[i] = count[j]
                        count[j] = words
                        words = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = words

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)