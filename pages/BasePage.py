class BasePage:
    def __init__(self, page):
        self.page = page

    def safe_fill(self, locator, value, description=""):
        # Safely fills a text input field after ensuring it is visible
        try:
            locator.wait_for(state="visible")
            locator.fill(value)
        except Exception as e:
            raise Exception(f"Failed to fill {description}: {e}")

    def safe_click(self, locator, description=""):
        # Safely clicks on an element after ensuring it is visible
        try:
            locator.wait_for(state="visible")
            locator.click()
        except Exception as e:
            raise Exception(f"Failed to click {description}: {e}")

    def safe_select(self, locator, value, description=""):
        # Safely selects a value from a dropdown element
        try:
            locator.wait_for(state="visible")
            locator.select_option(value)
        except Exception as e:
            raise Exception(f"Failed to select {description}: {e}")

    def assert_element_text(self, locator, expected_text, description=""):
        # Waits for the element to be visible and verifies that its text matches the expected text
        try:
            locator.wait_for(state="visible")
            actual = locator.text_content()
            assert actual == expected_text, f"Expected '{expected_text}' but got '{actual}'"
        except Exception as e:
            raise Exception(f"{description} validation failed: {e}")

    def element_exists(self, locator):
        # Checks if an element is attached to the DOM (exists on the page)
        try:
            locator.wait_for(state="attached", timeout=1000)
            return True
        except:
            return False

    def safe_check_radio(self, locator, description=""):
        # Safely checks a radio button and verifies it is selected
        try:
            locator.wait_for(state="visible")
            locator.check()
            assert locator.is_checked(), f"{description} radio button was not selected"
        except Exception as e:
            raise Exception(f"Failed to check {description}: {e}")
