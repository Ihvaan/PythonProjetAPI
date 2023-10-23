import requests


def test_search_artists():
    api_url = "http://127.0.0.1:8000"

    # Simulate a GET request to the /artists/ endpoint
    response = requests.get(f"{api_url}/artists/?name=Buddy Guy")

    # Assert the response status code (200 for success)
    assert response.status_code == 200

    # Assert the response content, you can check for specific data or structure
    assert "Buddy Guy" in print(response.json())
