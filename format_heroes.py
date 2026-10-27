# heroes.json, downloaded directly from the API, is extremely large with too much unneeded data for this project
# this file reads through it and produces a new JSON file with just the required data (hero names and numerical IDs)
# this won't be incredibly optimized because it doesn't need to be
import json
import requests

# first, download the heroes.json file to the current working directory
rawString: str = requests.get("https://api.deadlock-api.com/v1/assets/heroes")
with open("heroes.json", "w") as h:
    h.write(rawString.text)

# open JSON file
with open("heroes.json", "r") as f:
    heroData = json.load(f)
    # set up array used for heroes
    heroArray = []

    # loop through each hero
    for hero in heroData:

        # create a dictionary object for each hero with just their id and name
        heroNameId = {
            "name" : hero["name"],
            "id" : hero["id"]
        }

        # add this object to the array
        heroArray.append(heroNameId)
    
    # now that the array is filled out, serialize it to JSON
    json_output = json.dumps(heroArray, indent=4)

    # take this JSON and output it
    with open("heroesFiltered.json", "w") as f2:
        f2.write(json_output)


