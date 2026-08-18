# pages/base_page.py
from playwright.sync_api import Locator, Page


class BasePage:
    """Master Page Object parent class wrapping Playwright primitives."""

    def __init__(self, page: Page):
        # 'self' binds the Playwright page instance to this object
        self.page = page

    def navigate(self, path: str = ""):
        """Navigates to a target path or base URL."""
        self.page.goto(path)

    def find_element(self, selector: str) -> Locator:
        """Returns a Playwright Locator with built-in auto-waiting."""
        return self.page.locator(selector)

    def click(self, selector: str):
        """Waits for element readiness and clicks it."""
        self.find_element(selector).click()

    def type_text(self, selector: str, text: str):
        """Clears an input field and types new text."""
        locator = self.find_element(selector)
        locator.fill(text)

    def get_text(self, selector: str) -> str:
        """Extracts inner text from an element."""
        return self.find_element(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        """Checks if an element is visible on the screen."""
        return self.find_element(selector).is_visible()