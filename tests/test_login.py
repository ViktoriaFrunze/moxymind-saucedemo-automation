import pytest

def test_login_success(login_page, page):
    """Checking for successful authorization"""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Let's check that we've been redirected to the product page
    assert "inventory.html" in page.url


def test_login_locked_out_user(login_page):
    """Checking for a blocked user error"""
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    # Checking the error message
    error_text = login_page.error_message.inner_text()
    assert "Sorry, this user has been locked out" in error_text