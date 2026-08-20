# tests/test_network_mock.py
from playwright.sync_api import Page, Route


def test_mock_server_error(page: Page) -> None:
    """
    Verifies network interception by forcing an HTTP 500 response on a browser GET request.
    """
    # 1. INTERCEPT: Catch matching network requests made inside the browser
    page.route(
        "**/posts/1",
        lambda route: route.fulfill(
            status=500,
            content_type="application/json",
            json={"message": "Internal Server Error"}
        )
    )

    # 2. EXECUTE: Trigger request inside the browser DOM context
    response = page.goto("https://jsonplaceholder.typicode.com/posts/1")

    # 3. ASSERT: Confirm browser received our intercepted status code
    assert response is not None
    assert response.status == 500, f"Expected status 500, got {response.status}"


def test_mock_custom_payload(page: Page) -> None:
    """
    Verifies intercepting a browser fetch call and fulfilling it with a custom JSON payload.
    """
    mocked_data = {
        "userId": 999,
        "id": 1,
        "title": "Mocked Playwright Title",
        "body": "This payload was intercepted and injected by Playwright!"
    }

    # 1. INTERCEPT: Fulfill matching browser requests directly with custom payload
    page.route(
        "**/posts/1",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            json=mocked_data
        )
    )

    # 2. EXECUTE: Perform an in-browser fetch request
    data = page.evaluate("""async () => {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
        return await response.json();
    }""")

    # 3. ASSERT: Verify the injected payload was returned to the browser client
    assert data["userId"] == 999
    assert data["title"] == "Mocked Playwright Title"