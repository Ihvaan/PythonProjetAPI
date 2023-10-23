import requests

api_url = "http://127.0.0.1:8000"


def test_search_artists():
    # Simulate a GET request to the /artists/ endpoint
    response = requests.get(f"{api_url}/artists/?name=Buddy Guy")

    # Assert the response status code (200 for success)
    assert response.status_code == 200

    # Assert the response content, you can check for specific data or structure
    assert "Buddy Guy" == response.json()[0]["Name"]


def test_get_albums_by_artist_id():
    artist_id = 3
    response = requests.get(f"{api_url}/albums/?artist_id={artist_id}")
    assert response.status_code == 200


def test_get_tracks_by_album_id():
    album_id = 200
    response = requests.get(f"{api_url}/tracks/?album_id={album_id}")
    assert response.status_code == 200
