from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_button = page.locator('a[href="/login"]')
        self.logout_button = page.locator('a[href="/logout"]')
        self.logged_in_as = page.locator("text=Logged in as")
        self.products_button = page.locator('a[href="/products"]')

    def click_signup_login_button(self):
        self.safe_click(self.login_button, "'Signup / Login' Button")

    def click_logout_button(self):
        self.safe_click(self.logout_button, "Logout Button")

    def verify_logged_in(self, username):
        self.assert_element_text(self.logged_in_as, username, "Logged In Message")

    def click_products_button(self):
        self.safe_click(self.products_button, "'Products' Button")
