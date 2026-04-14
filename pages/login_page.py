class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators (element addresses on the page)
        self.username_field = page.locator('[data-test="username"]')
        self.password_field = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, password):
        self.username_field.fill(user)
        self.password_field.fill(password)
        self.login_button.click()