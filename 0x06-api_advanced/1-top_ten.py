#!/usr/bin/python3
"""1. Top Ten"""

import requests	

def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit."""
resInf = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),headers={"User-Agent": "My-User-Agent"},allow_redirects=False)
if resInf.status_code >= 300:
print("None")
else:
[print(child.get("data").get("title"))
for child in resInf.json().get("data").get("children")]
