import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_flow(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage
) -> None:
    """
    Validates complete user journey:
    Login -> Add to Cart -> Cart Verification -> Checkout Info -> Order Finish.
    """
    # 1. Login
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Add product & go to cart
    inventory_page.add_first_item_to_cart()
    inventory_page.click_element(".shopping_cart_link")

    # 3. Verify cart & proceed
    assert cart_page.get_cart_item_count() == 1
    cart_page.proceed_to_checkout()

    # 4. Complete checkout form & submit order
    checkout_page.fill_checkout_info("Adeoye", "Tester", "100001")
    checkout_page.finish_checkout()

    # 5. Assert successful purchase confirmation
    assert checkout_page.get_completion_message() == "Thank you for your order!"