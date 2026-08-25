# pages/sauce_login_page.py
from playwright.sync_api import Page


class SauceLoginPage:
    """Encapsulates locators and user actions for SauceDemo Login."""

    def __init__(self, page: Page):
        self.page = page
        # Locators recorded from CodeGen
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()