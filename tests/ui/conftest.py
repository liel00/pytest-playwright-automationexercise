import requests
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
import pytest


@pytest.fixture(scope="function")
def set_up_tear_down(page: Page) -> Page:
    try:
        # Set a specific viewport size
        page.set_viewport_size({"width": 1536, "height": 800})

        # Navigate to the homepage with a timeout
        page.goto("https://www.automationexercise.com/", timeout=10000)

        # Verify the correct URL has loaded
        expect(page).to_have_url("https://www.automationexercise.com/", timeout=5000)

        yield page

    except PlaywrightTimeoutError:
        pytest.fail("Page load or element lookup timed out – check your internet connection or server status.")
    except Exception as e:
        pytest.fail(f"Unexpected error during setup: {e}")


def delete_user_account(email, password):
    # Deletes a user account using the API by sending a DELETE request with email and password.
    url = "https://automationexercise.com/api/deleteAccount"
    payload = {
        "email": email,
        "password": password
    }
    response = requests.delete(url, data=payload)

    if response.status_code == 200 and "Account deleted!" in response.text:
        print(f"User '{email}' deleted successfully.")
    else:
        print(f"Failed to delete user '{email}'. Status code: {response.status_code}, Response: {response.text}")


@pytest.fixture(scope="session", autouse=True)
def cleanup_user():
    delete_user_account("testuser@AAA2.com", "Test@1234")
