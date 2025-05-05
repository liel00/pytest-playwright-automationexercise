from pages.BasePage import BasePage


class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name_input = page.locator('[data-qa="signup-name"]')
        self.email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.incorrect_error_message = page.locator("text=Your email or password is incorrect!")
        self.mr_radio = page.locator('#id_gender1')
        self.password_input = page.locator("#password")
        self.day_select = page.locator('[data-qa="days"]')
        self.month_select = page.locator('[data-qa="months"]')
        self.year_select = page.locator('[data-qa="years"]')
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.company_input = page.locator('[data-qa="company"]')
        self.address1_input = page.locator('[data-qa="address"]')
        self.address2_input = page.locator('[data-qa="address2"]')
        self.country_select = page.locator('[data-qa="country"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_number_input = page.locator('[data-qa="mobile_number"]')
        self.create_account_button = page.locator('[data-qa="create-account"]')
        self.account_created_message = page.locator('[data-qa="account-created"]')
        self.continue_button = page.locator('[data-qa="continue-button"]')

        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.login_password_input = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')

    def user_registration(self, name, email, password, day, month, year, first_name, last_name,
                          company, address1, address2, country, state, city, zipcode,
                          mobile_number):
        self.safe_fill(self.name_input, name, "Name")
        self.safe_fill(self.email_input, email, "Email")
        self.safe_click(self.signup_button, "Signup Button")
        self.safe_check_radio(self.mr_radio, "Mr. Radio Button")
        self.safe_fill(self.password_input, password, "Password")
        self.safe_select(self.day_select, day, "Day")
        self.safe_select(self.month_select, month, "Month")
        self.safe_select(self.year_select, year, "Year")

        self.safe_fill(self.first_name_input, first_name, "First Name")
        self.safe_fill(self.last_name_input, last_name, "Last Name")
        self.safe_fill(self.company_input, company, "Company")
        self.safe_fill(self.address1_input, address1, "Address 1")
        self.safe_fill(self.address2_input, address2, "Address 2")
        self.safe_select(self.country_select, country, "Country")
        self.safe_fill(self.state_input, state, "State")
        self.safe_fill(self.city_input, city, "City")
        self.safe_fill(self.zipcode_input, zipcode, "Zipcode")
        self.safe_fill(self.mobile_number_input, mobile_number, "Mobile Number")

        self.safe_click(self.create_account_button, "Create Account Button")
        self.assert_element_text(self.account_created_message, "Account Created!", "Account Created Message")
        self.safe_click(self.continue_button, "Continue Button")

    def user_login(self, email, password):
        self.safe_fill(self.login_email_input, email, "Login Email")
        self.safe_fill(self.login_password_input, password, "Login Password")
        self.safe_click(self.login_button, "Login Button")

    def verify_incorrect_login(self):
        self.assert_element_text(self.incorrect_error_message, "Your email or password is incorrect!",
                           "Incorrect Login Error Message")

