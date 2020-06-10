#!/user/bin/env python3

import json
import requests
import datetime
import os

now = datetime.datetime.now()
dir = "PlantPlaces/%s" % now.strftime("%Y-%m-%d")
if not os.path.exists(dir):
    os.makedirs(dir)

# Enter your Solar System API key here
#api_key = ""

# base_url variable to store url 
base_url = "https://api.le-systeme-solaire.net/rest/bodies/"

# Give city name [or coordinates] to be used in later calculations
city_name = "Bissett, CA"

# get method of requests module return response object
response = requests.get(base_url)

# json method of response object convert json format into python format data
r = response.json()

# store json to file
with open('%s/%s.json' % (dir, now.strftime("%H:%M:%S")), 'w') as file:
    json.dump(r, file)
