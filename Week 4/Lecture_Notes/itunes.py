import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

respond = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

#show it as a json format
o = respond.json()

# in results dict
for name in o["results"]:
    print(name["artistName"],end = " ") #show me the artistname keys
    print(name["trackName"])
