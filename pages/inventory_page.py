from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = ".inventory_container"
    TITLE = ".title"
    SORT_DROPDOWN = ".product_sort_container"
    ITEM_PRICES = ".inventory_item_price"
    ADD_TO_CART_BTN = "button[id^='add-to-cart']"
    ADD_BACKPACK_BTN = "#add-to-cart-sauce-labs-backpack"
    CART_BADGE = ".shopping_cart_badge"

    def is_loaded(self) -> bool:
        """Checks if the inventory container element is visible on the page."""
        return self.find_element(self.INVENTORY_CONTAINER).is_visible()

    def get_title_text(self) -> str:
        """Returns the main header title text (e.g., 'Products')."""
        return self.get_text(self.TITLE)

    def add_backpack_to_cart(self) -> None:
        """Clicks the Add to Cart button specifically for the Sauce Labs Backpack."""
        self.click_element(self.ADD_BACKPACK_BTN)

    def get_cart_count(self) -> str:
        """Returns the current number displayed on the cart badge."""
        return self.get_text(self.CART_BADGE)

    def get_cart_badge_count(self) -> str:
        """Alias for get_cart_count for backward compatibility."""
        return self.get_cart_count()

    def sort_products_by(self, option_value: str) -> None:
        """Sorts products using the inventory dropdown ('az', 'za', 'lohi', 'hilo')."""
        self.select_option_by_value(self.SORT_DROPDOWN, option_value)

    def get_all_prices(self) -> list[float]:
        """Parses all visible product prices into a list of floats."""
        price_texts = self.find_element(self.ITEM_PRICES).all_inner_texts()
        return [float(p.replace("$", "").strip()) for p in price_texts]

    def add_first_item_to_cart(self) -> None:
        """Clicks the Add to Cart button for the first product."""
        self.find_element(self.ADD_TO_CART_BTN).first.click()