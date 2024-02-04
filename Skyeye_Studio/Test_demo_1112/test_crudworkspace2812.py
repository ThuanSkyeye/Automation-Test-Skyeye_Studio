# test_crud_workspace.py
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Skyeye_Studio.Test1512.test_config2912 import log_on_failure, login

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

        # Step 2: Update Workspace
        with allure.step("Step 2: Update Workspace"):
            self.update_workspace("Update_TestWorkspace01", "Update_Skyeye_Telecom", login)

        # Step 3: Delete Workspace
        with allure.step("Step 3: Delete Workspace"):
            self.delete_workspace("Kentran212431302&", login)

    @allure.severity(allure.severity_level.CRITICAL)
    def create_workspace(self, name, description, login):
        # Step 1: Implement the logic to create a workspace
        element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

        # Example: Enter workspace details and click buttons to create a workspace
        text_field = login.find_element(By.XPATH, "//input[@name='name']")
        text_field.send_keys(name)

        textarea_field = login.find_element(By.XPATH, "//textarea[@name='description']")
        textarea_field.send_keys(description)

        next_button_xpath = "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'muiltr-19a5hzf')]"
        next_button = login.find_element(By.XPATH, next_button_xpath)
        next_button.click()

        # Add verification logic if needed
        expected_message = f"Thêm không gian làm việc {name} thành công"
        success_message_xpath = "//p[@id='notification-message']"
        success_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

        # Additional verification steps, if needed

        # Save the workspace name for later use
        self.workspace_name = name

    # @allure.severity(allure.severity_level.CRITICAL)
    # def update_workspace(self, updated_name, updated_description, login):
    #     # Step 2: Implement the logic to update a workspace
    #     workspace_name = self.workspace_name
    #     workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
    #     # Example: Locate and click the workspace to be updated, update details, and click buttons
    #     edit_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button"
    #     edit_button = login.find_element(By.XPATH, edit_button_xpath)
    #     edit_button.click()
    #
    #     # Update details like name, description, and click buttons
    #     input_element = WebDriverWait(login, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//input[@name='name' and @placeholder='Workspace Name']"))
    #     )
    #
    #     WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
    #     WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
    #
    #     login.execute_script("arguments[0].value = '';", input_element)
    #
    #     input_element.send_keys(updated_name)
    #     textarea_element = login.find_element(By.XPATH, "//textarea[@name='description' and @placeholder='(Optional)']")
    #     textarea_element.send_keys(Keys.CONTROL + "a")  # Chọn toàn bộ văn bản
    #     textarea_element.send_keys(Keys.BACKSPACE)  # Xóa văn bản đã chọn
    #     textarea_element.send_keys(updated_description)
    #
    #     button_element = login.find_element(By.XPATH,
    #                                         "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']")
    #     button_element.click()
    #
    #     expected_result_after_edit = "Successfully update workspace"
    #     result_element_after_edit_xpath = "//p[@id='notification-message' and contains(text(), 'Successfully update workspace')]"
    #     result_element_after_edit = WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, result_element_after_edit_xpath))
    #     )
    #     actual_result_after_edit = result_element_after_edit.text
    #     assert actual_result_after_edit == expected_result_after_edit, f"Expected: {expected_result_after_edit}, Actual: {actual_result_after_edit}"
    #
    #     # Additional verification steps, if needed
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # def delete_workspace(self, password, login):
    #     # Step 3: Implement the logic to delete a workspace
    #     workspace_name = self.workspace_name
    #     workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
    #     # Example: Locate and click the workspace to be deleted, enter password, and click delete button
    #     delete_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button[2]"
    #     delete_button = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
    #     delete_button.click()
    #
    #     password_input_xpath = "//input[@placeholder='Your password' and @type='password']"
    #     password_input = WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, password_input_xpath)))
    #     password_input.send_keys(password)
    #
    #     button_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[5]/button[2]"
    #     button = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    #     button.click()
    #
    #     expected_result_after_delete = "Successfully delete workspace"
    #     result_element_after_delete_xpath = "//p[@id='notification-message' and contains(text(), 'Successfully delete workspace')]"
    #     result_element_after_delete = WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, result_element_after_delete_xpath))
    #     )
    #     actual_result_after_delete = result_element_after_delete.text
    #     assert actual_result_after_delete == expected_result_after_delete, f"Expected: {expected_result_after_delete}, Actual: {actual_result_after_delete}"
    #
    #     # Additional verification steps, if needed
    #
    # def verify_workspace_details(self, expected_name, expected_description, login):
    #     # Implement the logic to verify workspace details after creation, update, or deletion
    #     # Example: Locate and verify workspace details using xpath or other locators
    #     name_xpath = f"//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='{expected_name}']"
    #     description_xpath = f"//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='{expected_description}']"
    #     WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, name_xpath + " | " + description_xpath))
    #     )
    #
    #     workspace_name_element = login.find_element(By.XPATH, name_xpath)
    #     actual_name = workspace_name_element.text
    #     assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"
    #
    #     description_element = login.find_element(By.XPATH, description_xpath)
    #     actual_description = description_element.text
    #     assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"

# Entry point for running the test
if __name__ == "__main__":
    pytest.main(["-s", "test_crud_workspace.py"])
