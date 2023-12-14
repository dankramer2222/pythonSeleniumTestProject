import pytest
from selenium.webdriver.common.by import By
import time


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        # Navigate to page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)
        # maximize window
        driver.maximize_window()

        # Type username student into username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        # Type password in the password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")
        # Push 'submit' button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(2)
        # Verify new page Url contains "practicetestautomation.com/logged-in-successfully/"
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        # Verify new page contains expected text ("Congratulations" or "successfully logged in"
        logedInText = driver.find_element(By.TAG_NAME, "h1")
        actual_text = logedInText.text
        assert actual_text == "Logged In Successfully"
        # Verify button Log out is displayed on new page
        logout = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout.is_displayed()
