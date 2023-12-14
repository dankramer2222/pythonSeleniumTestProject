import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        driver.find_element(By.ID, "add_btn").click()
        # Verify Row 2 input field is displayed
        wait = WebDriverWait(driver, 10)
        row_2_input_locator = driver.find_element(By.XPATH, "(//input[@class='input-field'])[2]")
        assert row_2_input_locator.is_displayed(), "Row2_input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_invalid_element_not_intractable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        driver.find_element(By.ID, "add_btn").click()
        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_2_input_locator = driver.find_element(By.XPATH, "(//input[@class='input-field'])[2]")
        # Type text into the second input field
        row_2_input_locator.send_keys("text")
        # Push Save button using locator By.name(“Save”)
        driver.find_element(By.XPATH, "//div[@id='row2']//button[@id='save_btn']").click()
        wait = WebDriverWait(driver, 5)
        # Verify text saved
        confirm = driver.find_element(By.ID, "confirmation")
        confirmation_message = confirm.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Clear input field
        driver.find_element(By.XPATH, "//button[@id='edit_btn']").click()
        # Type text into the input field
        input_field = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        input_field.clear()
        input_field.send_keys("cake")
        # Verify text changed
        confirm1 = input_field.get_attribute("value")
        assert confirm1 == "cake", "Expected 'cake', but got " + confirm1

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "Instruction text element should not be displayed")

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
                                         "Failed waiting for Row 2 input to be visible")

        # Verify second input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
