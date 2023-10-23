from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List

# We create the FastAPI application
app = FastAPI()

# We create the SQLite database and SQLAlchemy session
database_url = "sqlite:///chinook.db"
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We create a SQLAlchemy model class for artists
Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"
    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    albums = relationship("Album", back_populates="artist")


# We create a SQLAlchemy model class for albums
class Album(Base):
    __tablename__ = "albums"
    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"))
    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")


# We create a SQLAlchemy model class for tracks
class Track(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    album = relationship("Album", back_populates="tracks")


# FastAPI routes
@app.get("/artists/")
def search_artists_by_name(name: str):
    db = SessionLocal()
    artists = db.query(Artist).filter(Artist.Name.ilike(f"%{name}%")).all()
    db.close()
    return artists


@app.get("/albums/")
def get_albums_by_artist_id(artist_id: int):
    db = SessionLocal()
    albums = db.query(Album).filter(Album.ArtistId == artist_id).all()
    db.close()
    return albums


@app.get("/tracks/")
def get_tracks_by_album_id(album_id: int):
    db = SessionLocal()
    tracks = db.query(Track).filter(Track.AlbumId == album_id).all()
    db.close()
    return tracks
