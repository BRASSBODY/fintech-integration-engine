from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    CHECKOUT_BTN = "#checkout"
    CONTINUE_SHOPPING_BTN = "#continue-shopping"

    def get_cart_item_count(self) -> int:
        """Returns total number of items currently in the cart list."""
        return self.find_element(self.CART_ITEM).count()

    def get_first_item_name(self) -> str:
        """Fetches the title of the first item in the cart."""
        return self.get_text(self.ITEM_NAME)

    def proceed_to_checkout(self) -> None:
        """Clicks the Checkout button to advance to guest details."""
        self.click_element(self.CHECKOUT_BTN)