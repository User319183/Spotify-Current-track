
import spotipy
import spotipy.util as util
import json
import sys


token = "YOUR_API_TOKEN"

    
#use the token to connect to my account
spotifyObject = spotipy.Spotify(auth=token)

#get my current playing track
currentTrack = spotifyObject.current_user_playing_track()

#make sure it only prints the track name and artist
print("Right now, I'm listening to: ", currentTrack['item']['name'], "by", currentTrack['item']['artists'][0]['name'])



