def test_add_to_cart(login_page, inventory_page):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    # Let's check that the number 1 has appeared in the shopping cart
    assert inventory_page.cart_badge.inner_text() == "1"