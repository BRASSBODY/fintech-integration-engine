import pytest
from playwright.sync_api import Page, Playwright, BrowserContext, Browser
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.dynamic_loading_page import DynamicLoadingPage
from utils.api_client import APIClient


# --- Standard UI Fixtures ---

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)


# --- Storage State / Pre-Authed Fixtures ---

@pytest.fixture(scope="session")
def user_storage_state(tmp_path_factory, browser: Browser) -> str:
    """Logs in once per test session and saves the cookies/localstorage state."""
    state_path = tmp_path_factory.mktemp("state") / "state.json"
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    context.storage_state(path=str(state_path))
    context.close()
    return str(state_path)


@pytest.fixture
def authed_context(browser: Browser, user_storage_state: str) -> BrowserContext:
    """Creates a browser context pre-loaded with valid authentication state."""
    context = browser.new_context(storage_state=user_storage_state)
    yield context
    context.close()


@pytest.fixture
def authed_inventory_page(authed_context: BrowserContext) -> InventoryPage:
    """Provides an InventoryPage instance that opens directly pre-authenticated."""
    page = authed_context.new_page()
    inventory_page = InventoryPage(page)
    inventory_page.navigate("https://www.saucedemo.com/inventory.html")
    return inventory_page


@pytest.fixture
def dynamic_loading_page(page: Page) -> DynamicLoadingPage:
    return DynamicLoadingPage(page)
    

@pytest.fixture
def api_client(playwright: Playwright) -> APIClient:
    """Provides an isolated HTTP client using Playwright APIRequestContext."""
    context = playwright.request.new_context()
    client = APIClient(request=context, base_url="https://jsonplaceholder.typicode.com")
    yield client
    context.dispose()