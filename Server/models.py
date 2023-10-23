# We import the necessary modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# We create a base SQLAlchemy model class
Base = declarative_base()


# The Artist class is a representation of the "artists" table in the database
class Artist(Base):
    # We specify the name of the table in the database
    __tablename__ = "artists"

    # We create the columns of the "artists" table with their data types
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

    # We establish a relationship with the Album class to retrieve albums associated with an artist
    albums = relationship("Album", back_populates="artist")


class Album(Base):
    __tablename__ = "albums"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"))
    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")


class Track(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    album = relationship("Album", back_populates="tracks")
