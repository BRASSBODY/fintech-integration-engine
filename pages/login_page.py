# pages/login_page.py
from config import settings
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Page."""

    def __init__(self, page):
        super().__init__(page)

        # LOCATORS (Control Panel Wiring)
        self._username_input = "#user-name"
        self._password_input = "#password"
        self._login_button = "#login-button"
        self._error_message = "h3[data-test='error']"

    # ACTIONS (Driver Controls)
    def load(self):
        """Opens the login page URL."""
        self.navigate(settings.BASE_URL)

    def login(self, username: str = settings.STANDARD_USER, password: str = settings.PASSWORD):
        """Fills credentials and submits the login form."""
        self.type_text(self._username_input, username)
        self.type_text(self._password_input, password)
        self.click(self._login_button)

    def get_error_message(self) -> str:
        """Retrieves text from the error banner on failed login."""
        return self.get_text(self._error_message)