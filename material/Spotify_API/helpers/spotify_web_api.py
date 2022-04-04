import requests
import pprint

TOKEN = "BQDAvNu8NmtrE_sYkao1y_8E_LaOLuwdyGn8dSNnrNiT-BrdVAtz2bqz3RFFIxT-27OzRhU3pF9hNb4rJolN1xjyxBNFi6pGcfdQUfIXsKAEh30InNpOotloZozwLMsB-oZ-vcB6M8U8"

def search(query):
    r = requests.get(url="https://api.spotify.com/v1/search",
                     params={"q": query, "type": "album,artist,playlist,track,show,episode"},
                     headers={"Authorization": "Bearer " + TOKEN})

    response = {
        "Count": 0,
        "Records": []
    }

    for key in ["tracks", "artists", "albums", "playlists", "shows", "episodes"]:
        if key in r.json():
            response["Count"] = response["Count"] + len(r.json()[key]["items"])

            for item in r.json()[key]["items"]:
                response["Records"].append(item)

    return response

def artist(id):
    r = requests.get(url=f"https://api.spotify.com/v1/artists/{id}", headers={"Authorization": "Bearer " + TOKEN})
    return r.json()