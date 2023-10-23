# We import the necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Artist, Album, Track

# Database URL
database_url = "sqlite:///chinook.db"

# We create an SQLAlchemy engine for the database
engine = create_engine(database_url)

# We create an SQLAlchemy session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Get artists by name
def get_artists_by_name(name):
    # We open a database session
    db = SessionLocal()

    # We use the session to query artists whose name contains the "name" string
    artists = db.query(Artist).filter(Artist.Name.like(f"%{name}%")).all()

    # We close the database session to release resources
    db.close()

    # We return the found artists
    return artists


# Get albums by artist ID
def get_albums_by_artist_id(artist_id):
    db = SessionLocal()
    albums = db.query(Album).filter(Album.ArtistId == artist_id).all()
    db.close()
    return albums


# Get tracks by album ID
def get_tracks_by_album_id(album_id):
    db = SessionLocal()
    tracks = db.query(Track).filter(Track.AlbumId == album_id).all()
    db.close()
    return tracks
