# tests/test_auth.py
from config import settings
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_successful_login(login_page: LoginPage, inventory_page: InventoryPage):
    """Verifies that a user with valid credentials can log in successfully."""
    # 1. Arrange & Act
    login_page.load()
    login_page.login(username=settings.STANDARD_USER, password=settings.PASSWORD)

    # 2. Assert
    assert inventory_page.is_loaded(), "Inventory container failed to render post-login."
    assert inventory_page.get_title_text() == "Products", f"Expected title 'Products', got '{inventory_page.get_title_text()}'"


def test_locked_out_user_login(login_page: LoginPage):
    """Verifies that a locked-out user receives an appropriate error message."""
    # 1. Arrange & Act
    login_page.load()
    login_page.login(username=settings.LOCKED_USER, password=settings.PASSWORD)

    # 2. Assert
    error_text = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out." in error_text


def test_add_item_to_cart(login_page: LoginPage, inventory_page: InventoryPage):
    """Verifies that logging in and clicking 'Add to Cart' updates the cart badge."""
    # 1. Arrange & Act
    login_page.load()
    login_page.login(username=settings.STANDARD_USER, password=settings.PASSWORD)
    inventory_page.add_backpack_to_cart()

    # 2. Assert
    assert inventory_page.get_cart_count() == "1", "Cart badge count did not update to '1'."