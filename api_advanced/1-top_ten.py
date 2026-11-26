#!/usr/bin/python3
"""Queries the Reddit API for the top ten hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a subreddit.

    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0"}
    try:
        response = requests.get(url, headers=headers, params={"limit": 10},
                                allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children", [])
    except Exception:
        print(None)
        return
    if not posts:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
