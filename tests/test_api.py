from utils.api_client import APIClient


def test_get_post(api_client: APIClient) -> None:
    """Verifies GET endpoint returns status 200 and expected data structure."""
    response = api_client.get("/posts/1")
    
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data


def test_create_post(api_client: APIClient) -> None:
    """Verifies POST endpoint accepts JSON payload and creates resource."""
    payload = {"title": "QA Automation", "body": "Playwright API testing", "userId": 1}
    response = api_client.post("/posts", payload)
    
    assert response.status == 201
    assert response.json()["title"] == "QA Automation"