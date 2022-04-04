from helpers import spotify_web_api, system_history
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

FILE_PATH = "./system_history/system_history.json"

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/api/search")
async def api_search(q: str = "", token: str = Depends(oauth2_scheme)):
    if token == "":
        return {"message": "Error! No user token provided."}
    elif q == "":
        return {"message": "Error! No query search provided."}

    system_history.log_system_history_action(file_path=FILE_PATH, token=token, action=f"/api/search?q={q}")

    return spotify_web_api.search(query=q)

@app.get("/api/artist/{spotify_artists_id}")
async def artist_api(spotify_artists_id: str = "", token: str = Depends(oauth2_scheme)):
    if token == "":
        return {"message": "Error! No user token provided."}

    system_history.log_system_history_action(file_path=FILE_PATH, token=token, action=f"/api/artist/{spotify_artists_id}")

    return spotify_web_api.artist(id=spotify_artists_id)

@app.get("api/system/history")
async def system_history_api(token: str = Depends(oauth2_scheme)):
    if token == "":
        return {"message": "Error! No user token provided."}

    # TODO