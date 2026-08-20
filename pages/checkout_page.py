from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Form Inputs
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BTN = "#continue"

    # Overview & Finish
    FINISH_BTN = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fills out the checkout information form and clicks continue."""
        self.fill_text(self.FIRST_NAME_INPUT, first_name)
        self.fill_text(self.LAST_NAME_INPUT, last_name)
        self.fill_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click_element(self.CONTINUE_BTN)

    def finish_checkout(self) -> None:
        """Clicks finish on the order summary page."""
        self.click_element(self.FINISH_BTN)

    def get_completion_message(self) -> str:
        """Returns the confirmation header text after completing checkout."""
        return self.get_text(self.COMPLETE_HEADER)