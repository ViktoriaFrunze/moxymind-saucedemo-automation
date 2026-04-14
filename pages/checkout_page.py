class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.zip_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('.complete-header')

    def fill_customer_info(self, first, last, zip):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()