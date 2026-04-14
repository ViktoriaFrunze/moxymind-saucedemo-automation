# Configuration for tests
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

from pages.inventory_page import InventoryPage

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

from pages.checkout_page import CheckoutPage

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)