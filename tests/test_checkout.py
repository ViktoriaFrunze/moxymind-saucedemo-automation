def test_end_to_end_checkout(login_page, inventory_page, checkout_page):
    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Add to cart and go to the cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    # 3. Click “Checkout”
    inventory_page.page.locator('[data-test="checkout"]').click()

    # 4. Entering data
    checkout_page.fill_customer_info("Moxy", "Mind", "12345")

    # 5. Conclusion
    checkout_page.finish_checkout()

    # 6. Success Check
    assert checkout_page.complete_header.inner_text() == "Thank you for your order!"