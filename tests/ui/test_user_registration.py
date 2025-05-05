import pytest
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage


@pytest.mark.sanity
def test_user_registration_and_login(set_up_tear_down, page) -> None:
    """ This test verifies that a user can register and then log in successfully."""
    home_page = HomePage(page)
    home_page.click_signup_login_button()

    singup_page = SignUpPage(page)
    singup_page.user_registration(
        name="Liel1993",
        email="testuser@AAA2.com",
        password="Test@1234",
        day="10",
        month="5",
        year="1990",
        first_name="Test",
        last_name="User",
        company="TestCompany",
        address1="123 Test St",
        address2="Apt 456",
        country="Canada",
        state="Ontario",
        city="Toronto",
        zipcode="123456",
        mobile_number="1234567890")

    home_page.click_logout_button()
    home_page.click_signup_login_button()
    singup_page.user_login("testuser@AAA2.com", "Test@1234")
    home_page.verify_logged_in(' Logged in as Liel1993')
