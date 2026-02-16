#!/usr/bin/env python3

import os
import json
import requests

def main():
    GHUSER = os.getenv('GITHUB_USER')
    url = f'https://api.github.com/users/{GHUSER}/events'
    r = json.loads(requests.get(url).text)

    for x in r[:5]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

if __name__ == "__main__":
    main()