import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
import random

client_id = 'b198c8bd8a574babbc49616d3b0f46c1'
client_secret_id = 'fbcdc5acddb3490795c007d08c541f4d'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret_id)

spotify_object = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print("Spotify API Connected")

def play_song(song):
  results = spotify_object.search(song,1,0,'track')
  song_dict = results['tracks']
  song_items = song_dict['items']
  if not song_items:
    print('Enter valid song')
    return
  song = song_items[0]['external_urls']['spotify']
  webbrowser.open(song)
  print('Song is opened in the browser')

def play_from_playlist(playlist_uri):
  playlist_tracks = spotify_object.playlist_tracks(playlist_uri)
  random_track = random.choice(playlist_tracks['items'])
  song = random_track['track']['external_urls']['spotify']
  print('Random Song returned')
  return song