# Spotify\_Web\_API
## Instructions

To execute this app, you should have installed the package [Uvicorn](https://www.uvicorn.org/). Then, the following instruction must be executed, from the app directory:

```bash
 uvicorn spotify_api:app
```

## Spotify API Requirements

To make requests to the Spotify API, a token must be sent. During the development of this application, a sample token has been set, but this one doesn't last much.

To regenerate the token, you must go to [Search for Item | Spotify for Developers](https://developer.spotify.com/console/get-search-item/), and generate a sample token from the form. A Spotify account could be required.

Once this token has been regenerated, you must go to the file `./helpers/spotify_web_api.py`, located in the application project, and change the value of the constant `TOKEN`, located at the file's **line #4**.

## API Ports
### Search: api/search?q={term}

To access to this API port, a query value (`q`) must be set. Additionally, a Bearer Token must also be sent during the request.

### Artist: api/artist/{spotify_artists_id}

To access to this API port, a valid Spotify artist ID must be set. To search one valid, head to Spotify, search for an artist of your choice, and copy the ID that is included in the URL. Additionally, a Bearer Token must also be sent during the request.

### System History: api/system/history

To access to this API port, a Bearer Token must be sent during the request.