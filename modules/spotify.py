"""
Spotify Plugin, move to plugin folder later
Add API/exports to this to make it module
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

client_id = ""
client_secret = ""
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
sp.start_playback(uris=['spotify:track:210JJAa9nJOgNa0YNrsT5g']) # new jeans gods