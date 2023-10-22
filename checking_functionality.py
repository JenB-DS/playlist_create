import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these with your own credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Authenticate with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example: Search for a track
results = sp.search(q='Your search query', type='track')
track_name = results['tracks']['items'][0]['name']
print(f"First track found: {track_name}")
