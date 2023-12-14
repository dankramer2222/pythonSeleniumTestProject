import pytest
from selenium.webdriver.common.by import By
import time


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [
        ("incorrectUser", "Password123", "Your username is invalid!"),
        ("student", "incorrectPassword", "Your password is invalid!")
    ])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Type username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        # Press Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed as expected"

        # Verify error message text is as expected
        error_message_text = error_message.text
        assert error_message_text == expected_error_message, "Error message is not as expected"

    def test_negative_username(self, driver):
        # Type username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")

        # Press Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed as expected"

        # Verify error message text is Your username is invalid!
        error_message_text = error_message.text
        assert error_message_text == "Your username is invalid!", "Error message is not as expected"

    def test_negative_password(self, driver):
        # Type username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("incorrectPassword")

        # Press Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed as expected"

        # Verify error message text is Your password is invalid!
        error_message_text = error_message.text
        assert error_message_text == "Your password is invalid!", "Error message is not as expected"
