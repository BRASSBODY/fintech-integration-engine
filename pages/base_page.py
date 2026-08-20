from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigates to URL as soon as DOM content loads, preventing network timeouts."""
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def find_element(self, selector: str) -> Locator:
        """Returns a Playwright Locator object."""
        return self.page.locator(selector)

    def click_element(self, selector: str) -> None:
        """Clicks on an element matching the selector."""
        self.page.locator(selector).click()

    def fill_text(self, selector: str, text: str) -> None:
        """Fills text into an input field."""
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """Returns inner text of an element."""
        return self.page.locator(selector).inner_text()

    def select_option_by_value(self, selector: str, value: str) -> None:
        """Selects an option from a standard HTML <select> dropdown by value."""
        self.page.locator(selector).select_option(value=value)