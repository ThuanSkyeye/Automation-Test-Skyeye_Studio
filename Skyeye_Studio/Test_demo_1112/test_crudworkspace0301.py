import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_config2912 import log_on_failure, login

# Fixture to handle the log_on_failure functionality
@pytest.fixture
def log_on_failure_fixture(log_on_failure):
    # Use the log_on_failure fixture from test_config
    yield log_on_failure

# Test class for Workspace Management
@pytest.mark.usefixtures("log_on_failure_fixture")
class TestWorkspaceManagement:
    def setup_method(self):
        self.workspace_name = ""

    # Test method for creating, updating, and deleting a workspace
    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Create, Update, and Delete Workspace")
    def test_create_update_delete_workspace(self, login):
        # Step 1: Create Workspace
        with allure.step("Step 1: Create Workspace"):
            self.create_workspace("TestWorkspace01", "Skyeye_Telecom", login)

    @allure.severity(allure.severity_level.CRITICAL)
    def create_workspace(self, name, description, login):
        # Step 1: Wait for the page to load
        element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

        # Step 2: Fill in the workspace details
        with allure.step("Enter Workspace Details"):
            text_field = login.find_element(By.XPATH, "//input[@name='name']")
            text_field.send_keys(name)

            textarea_field = login.find_element(By.XPATH, "//textarea[@name='description']")
            textarea_field.send_keys(description)

        # Step 3: Click the 'Next' button
        with allure.step("Click 'Next' Button"):
            next_button_xpath = "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'muiltr-19a5hzf')]"
            next_button = login.find_element(By.XPATH, next_button_xpath)
            next_button.click()

        # Step 4: Verify the success message
        with allure.step("Verify Success Message"):
            success_message_xpath = "//p[@id='notification-message' and contains(text(), 'Thêm không gian làm việc thành công')]"
            success_message = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.XPATH, success_message_xpath))
            )
            actual_message = success_message.text
            expected_message = f"Thêm không gian làm việc {name} thành công"
            assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

        # Step 5: Additional verification steps, if needed

        # Step 6: Save the workspace name for later use
        self.workspace_name = name
