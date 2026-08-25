# tests/test_sauce_login.py
from playwright.sync_api import Page
from pages.sauce_login_page import SauceLoginPage


def test_sauce_login_success(page: Page) -> None:
    """Validates successful login using the refactored POM class."""
    login_page = SauceLoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Assert navigation reached the inventory page
    assert page.url == "https://www.saucedemo.com/inventory.html"