import pytest
from pages.inventory_page import InventoryPage


def test_sort_products_by_price_low_to_high(
    authed_inventory_page: InventoryPage
) -> None:
    """
    Verifies sorting on pre-authenticated session directly without UI login delay.
    """
    # Direct Action (already on inventory page, logged in)
    authed_inventory_page.sort_products_by("lohi")

    # Fetch & Verify
    prices = authed_inventory_page.get_all_prices()
    assert prices == sorted(prices), f"Prices not sorted low-to-high: {prices}"