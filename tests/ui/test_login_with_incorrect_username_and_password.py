from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
import pytest


@pytest.mark.parametrize("email, password", [
    ("LielTest1993@gmail.com", "1234345"),  # Correct email and incorrect password
    ("LielTest1991@gmail.com", "123456"),   # Correct password and incorrect email
    ("admin'+OR+'1'='1'@example.com", "any_password"),  # SQL Injection attempt
])
@pytest.mark.sanity
def test_login_with_incorrect_username_and_password(set_up_tear_down, page, email, password) -> None:
    """ This test verifies that logging in with incorrect credentials shows the appropriate error message."""

    signup_page = SignUpPage(page)
    home_page = HomePage(page)

    home_page.click_signup_login_button()
    signup_page.user_login(email, password)
    signup_page.verify_incorrect_login()
