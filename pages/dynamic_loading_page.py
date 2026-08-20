from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    START_BUTTON = "#start button"
    LOADING_SPINNER = "#loading"
    FINISH_TEXT = "#finish h4"

    def start_process(self) -> None:
        """Clicks start to trigger the asynchronous loading process."""
        self.click_element(self.START_BUTTON)

    def wait_for_loading_to_complete(self) -> None:
        """Explicitly waits until the loading spinner disappears from the DOM."""
        self.page.locator(self.LOADING_SPINNER).wait_for(state="hidden")

    def get_finish_text(self) -> str:
        """Retrieves text once the dynamic loading finishes."""
        self.page.locator(self.FINISH_TEXT).wait_for(state="visible")
        return self.get_text(self.FINISH_TEXT)