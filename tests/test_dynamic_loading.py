import pytest
from pages.dynamic_loading_page import DynamicLoadingPage


def test_wait_for_dynamic_element(dynamic_loading_page: DynamicLoadingPage) -> None:
    """
    Validates handling asynchronous loading spinners and delayed UI elements.
    """
    # 1. Navigate to dynamic loading demo page
    dynamic_loading_page.navigate("https://the-internet.herokuapp.com/dynamic_loading/1")

    # 2. Trigger loading
    dynamic_loading_page.start_process()

    # 3. Synchronize on element state
    dynamic_loading_page.wait_for_loading_to_complete()

    # 4. Verify loaded text
    assert dynamic_loading_page.get_finish_text() == "Hello World!"