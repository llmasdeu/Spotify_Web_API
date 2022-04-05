import requests

TOKEN = "BQBi3LGxRatqA_tY5JWE1mGkic4It9nno0d4CEe4O6mmwkqkxI6XTEDDe43guFiOmQyZMKumoTZRaqopO6eEEfX3tBGbI5MnDzxw4fsXj6MuS9vUkang9TqfY4TpELsm10VtuaDW11wv"

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