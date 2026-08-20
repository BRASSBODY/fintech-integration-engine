from playwright.sync_api import APIRequestContext, APIResponse


class APIClient:
    def __init__(self, request: APIRequestContext, base_url: str) -> None:
        self.request = request
        self.base_url = base_url

    def get(self, endpoint: str) -> APIResponse:
        """Executes an HTTP GET request."""
        return self.request.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint: str, payload: dict) -> APIResponse:
        """Executes an HTTP POST request with a JSON payload."""
        return self.request.post(f"{self.base_url}{endpoint}", data=payload)