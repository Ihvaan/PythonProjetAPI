# We import model classes from the Server.models module, which allows us to use the same model classes for both API data and the database
import requests
from Server.models import Album, Artist, Track

# FastAPI API URL
api_url = "http://localhost:8000"


# Search artists by name
def search_artists_by_name(name):
    # Make a GET request to the API to search for artists by name
    response = requests.get(f"{api_url}/artists/?name={name}")
    if response.status_code == 200:
        artists = response.json()
        print("Artists found:")
        for artist in artists:
            print(f"Artist ID: {artist['ArtistId']}, Name: {artist['Name']}")
    else:
        print("Error:", response.status_code, response.text)


# Get albums by artist ID
def get_albums_by_artist_id(artist_id):
    # Make a GET request to the API to get albums by artist ID
    response = requests.get(f"{api_url}/albums/?artist_id={artist_id}")
    if response.status_code == 200:
        albums = response.json()
        print("Albums for Artist ID", artist_id)
        for album in albums:
            print(f"Album ID: {album['AlbumId']}, Title: {album['Title']}")
    else:
        print("Error:", response.status_code, response.text)


# Get tracks by album ID
def get_tracks_by_album_id(album_id):
    # Make a GET request to the API to get tracks by album ID
    response = requests.get(f"{api_url}/tracks/?album_id={album_id}")
    if response.status_code == 200:
        tracks = response.json()
        print("Tracks for Album ID", album_id)
        for track in tracks:
            print(f"Track ID: {track['TrackId']}, Name: {track['Name']}")
    else:
        print("Error:", response.status_code, response.text)


# Provide instructions to the user
if __name__ == "__main__":
    option = input(
        "Choose an option:\n1. Search artists by name\n2. Get albums by artist ID\n3. Get tracks by album ID\n"
    )
    if option == "1":
        name = input("Enter the artist name: ")
        search_artists_by_name(name)
    elif option == "2":
        artist_id = int(input("Enter the artist ID: "))
        get_albums_by_artist_id(artist_id)
    elif option == "3":
        album_id = int(input("Enter the album ID: "))
        get_tracks_by_album_id(album_id)
    else:
        print("Invalid option")
