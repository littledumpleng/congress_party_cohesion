#!/usr/bin/env python3

import sys
import json
import requests

def get(url, key):
    headers = {"X-API-KEY": key}
    url = "http://api.propublica.org/congress/v1" + url #querying version 1 of API # + url is variable
    data = requests.get(url, headers = headers).json() #gets full-text html of url's webpage. pass in headers dictionary containing API key. converts to json
    #print(json.dumps(data, indent = 2)) #dumps to a string with an indentation of two spaces
    return data['results']

if __name__ == "__main__":
    with open('key.txt') as handle:
        key = handle.read().strip() #strips trailing \n characters
    
    for congress in range(111, 117):
        percentages = []
        for response in get(f"/{congress}/senate/members.json", key): #example: f"/116/senate/members.json"
            for member in response['members']: #will display votes with party % for each politician
                percentages.append(member['votes_with_party_pct'])
        avg_cohesion = sum(percentages)/len(percentages)
        print(congress, avg_cohesion)