import meetup.api
import json
import requests
import time
import os
import yaml

import pprint


cities =[("San Francisco", "CA"),("Seattle","WA"),("New York","NY"),("Denver","CO")]
api_key= '175b5b5576142b4442605f7d502252c'

for (city, state) in cities:
    count = 0
    per_page = 4
    offset = 0
    results_we_got = per_page
    while (results_we_got == per_page):
        params=({"sign":"true","country":"US", "city":city, "state":state, "radius": 10, "key":api_key, "page":per_page,"offset":offset})
        time.sleep(1)
        # https://www.meetup.com/meetup_api/
        # Documentation: https://www.meetup.com/meetup_api/docs/2/groups/
        request = requests.get("http://api.meetup.com/2/groups",params=params)
        data = request.json()
        offset += 1
        results_we_got = data['meta']['count']
        pprint.pprint(data['results'][0])
    time.sleep(1)