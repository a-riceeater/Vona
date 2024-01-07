"""
Spotify Plugin, move to plugin folder later
Add API/exports to this to make it module
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()


client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = "http://ghwosty.com" # replace with github pages url requesting URL
scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id=client_id,
          client_secret=client_secret,
          redirect_uri=redirect_uri,    
          scope=scope, open_browser=False))

# Shows playing devices
res = sp.devices()
print(res)

# Change track
#sp.start_playback(uris=['spotify:track:210JJAa9nJOgNa0YNrsT5g']) # new jeans gods

def getTrackId(title, artist, album=""):
   results = sp.search(limit=1, type="track", q=f"{title}%20{artist}", offset=0)
   if results['tracks']['items']:
       return results
       #return results['tracks']['items'][0]['id']
   else:
       return results


print(getTrackId("gods", "new jeans"))