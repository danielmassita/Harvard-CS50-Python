import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit

# Change before/after the limit=1 to limite=50 (for Top10)
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

print(response.json())
print("")
print(json.dumps(response.json(), indent=2))

# Now, from the API from itunes, we used JSON to request some dictionary! :)

o = response.json()
for result in o["results"]:
    print(result["trackName"])