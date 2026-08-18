# pages/inventory_page.py
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # Use data-test attribute to strictly select the outer inventory container
        self._inventory_container = '[data-test="inventory-container"]'
        self._title = '[data-test="title"]'
        self._add_backpack_btn = '[data-test="add-to-cart-sauce-labs-backpack"]'
        self._cart_badge = '[data-test="shopping-cart-badge"]'

    def is_loaded(self) -> bool:
        return self.is_visible(self._inventory_container)

    def get_title_text(self) -> str:
        return self.get_text(self._title)

    def add_backpack_to_cart(self):
        self.click(self._add_backpack_btn)

    def get_cart_count(self) -> str:
        return self.get_text(self._cart_badge)