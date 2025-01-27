import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Replace these with your Spotify Developer credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback'  # Default redirect URI

# Scope required to create and modify playlists
SCOPE = 'playlist-modify-public'

# CSV file path
CSV_FILE = 'personalized_playlist.csv'

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# Step 1: Read the CSV file
print("Reading CSV file...")
df = pd.read_csv(CSV_FILE)

# Ensure columns for track and artist names are correctly named
TRACK_COLUMN = 'master_metadata_track_name'
ARTIST_COLUMN = 'master_metadata_album_artist_name'

# Step 2: Search for tracks on Spotify
def get_track_uris(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    return None

print("Searching for tracks on Spotify...")
track_uris = []
for _, row in df.iterrows():
    track_uri = get_track_uris(row[TRACK_COLUMN], row[ARTIST_COLUMN])
    if track_uri:
        track_uris.append(track_uri)
    else:
        print(f"Track not found: {row[TRACK_COLUMN]} by {row[ARTIST_COLUMN]}")


# Step 3: Create a new playlist
USER_ID = sp.current_user()['id']
PLAYLIST_NAME = 'Personalized Playlist'
PLAYLIST_DESCRIPTION = 'A playlist created using my personalized recommendations.'

print("Creating a new playlist...")
playlist = sp.user_playlist_create(
    user=USER_ID,
    name=PLAYLIST_NAME,
    public=True,
    description=PLAYLIST_DESCRIPTION
)

# Step 4: Add tracks to the playlist
if track_uris:
    print(f"Adding {len(track_uris)} tracks to the playlist...")
    sp.user_playlist_add_tracks(user=USER_ID, playlist_id=playlist['id'], tracks=track_uris)
    print(f"Playlist '{PLAYLIST_NAME}' created successfully!")
else:
    print("No valid tracks found to add to the playlist.")
