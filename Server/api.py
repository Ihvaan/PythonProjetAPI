# We import FastAPI and functions to retrieve data from the database
from fastapi import FastAPI, Query
from typing import List
from database import (
    get_artists_by_name,
    get_albums_by_artist_id,
    get_tracks_by_album_id,
)

# We create the FastAPI application
app = FastAPI()


# This route is used to search for artists by name
@app.get("/artists/")
async def search_artists(
    name: str = Query(description="Name of the artist to search for"),
):
    # We call the get_artists_by_name function to retrieve artists based on the name
    artists = get_artists_by_name(name)
    return artists


# Retrieve albums by artist ID
@app.get("/albums/")
async def get_albums(artist_id: int = Query(description="Artist ID")):
    albums = get_albums_by_artist_id(artist_id)
    return albums


# Retrieve tracks by album ID
@app.get("/tracks/")
async def get_tracks(album_id: int = Query(description="Album ID")):
    tracks = get_tracks_by_album_id(album_id)
    return tracks
