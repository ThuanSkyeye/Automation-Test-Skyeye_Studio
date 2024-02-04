import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from test_config import login_fixture
from test_config import log_on_failure

class TestWorkspaceManagement:
    def setup_method(self):
        self.workspace_name = ""

    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Create, Update, and Delete Workspace")
    def test_create_update_delete_workspace(self, login_fixture, log_on_failure):
        driver = login_fixture

        # Step 1: Create Workspace
        with allure.step("Step 1: Create Workspace"):
            self.create_workspace(driver, "TestWorkspace01", "Skyeye_Telecom")

        # Step 2: Update Workspace
        with allure.step("Step 2: Update Workspace"):
            self.update_workspace(driver, "Update_TestWorkspace01", "Update_Skyeye_Telecom")

        # Step 3: Delete Workspace
        with allure.step("Step 3: Delete Workspace"):
            self.delete_workspace(driver, "Kentran212431302$")

    @allure.severity(allure.severity_level.CRITICAL)
    def create_workspace(self, driver, name, description):
        element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

        element = driver.find_element(By.XPATH, element_xpath)
        element.click()

        text_field = driver.find_element(By.XPATH, "//input[@name='name']")
        text_field.send_keys(name)

        textarea_field = driver.find_element(By.XPATH, "//textarea[@name='description']")
        textarea_field.send_keys(description)

        next_button_xpath = "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'muiltr-19a5hzf')]"
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        next_button.click()

        expected_message = f"Successfully add workspace {name}"
        success_message_xpath = "//p[@id='notification-message']"
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

        # Additional verification steps, if needed
        self.verify_workspace_details(driver, name, description)

        # Attach expected and actual results to the Allure report for Create Workspace
        allure.attach(f"Expected Result - Create Workspace: {expected_message}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Create Workspace: {actual_message}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Expected Result - Workspace Name: {name}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Workspace Name: {name}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Expected Result - Workspace Description: {description}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Workspace Description: {description}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)

        # Lưu lại tên workspace
        self.workspace_name = name

    @allure.severity(allure.severity_level.CRITICAL)
    def update_workspace(self, driver, updated_name, updated_description):
        workspace_name = self.workspace_name
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
        wait = WebDriverWait(driver, 10)
        workspace_span = wait.until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

        edit_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button"
        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))
        edit_button.click()

        input_element = driver.find_element(By.XPATH, "//input[@name='name' and @placeholder='Workspace Name']")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))

        driver.execute_script("arguments[0].value = '';", input_element)

        input_element.send_keys(updated_name)
        textarea_element = driver.find_element(By.XPATH, "//textarea[@name='description' and @placeholder='(Optional)']")
        textarea_element.send_keys(Keys.CONTROL + "a")  # Chọn toàn bộ văn bản
        textarea_element.send_keys(Keys.BACKSPACE)  # Xóa văn bản đã chọn
        textarea_element.send_keys(updated_description)

        button_element = driver.find_element(By.XPATH,
                                            "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']")
        button_element.click()

        expected_result_after_edit = "Successfully update workspace"
        result_element_after_edit_xpath = "//p[@id='notification-message' and contains(text(), 'Successfully update workspace')]"
        result_element_after_edit = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, result_element_after_edit_xpath))
        )
        actual_result_after_edit = result_element_after_edit.text
        assert actual_result_after_edit == expected_result_after_edit, f"Expected: {expected_result_after_edit}, Actual: {actual_result_after_edit}"

        # Additional verification steps, if needed
        self.verify_workspace_details(driver, updated_name, updated_description)

        # Attach expected and actual results to the Allure report for Update Workspace
        allure.attach(f"Expected Result - Update Workspace: {expected_result_after_edit}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Update Workspace: {actual_result_after_edit}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Expected Result - Updated Workspace Name: {updated_name}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Updated Workspace Name: {updated_name}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Expected Result - Updated Workspace Description: {updated_description}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Updated Workspace Description: {updated_description}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.severity(allure.severity_level.CRITICAL)
    def delete_workspace(self, driver, password):
        workspace_name = self.workspace_name
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
        workspace_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

        delete_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button[2]"
        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
        delete_button.click()

        delete_button_xpath = "//span[contains(text(),'Delete')]"
        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
        delete_button.click()

        password_input_xpath = "//input[@placeholder='Your password' and @type='password']"
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_input_xpath)))
        password_input.send_keys(password)

        button_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[5]/button[2]"
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

        expected_result_after_delete = "Successfully delete workspace"
        result_element_after_delete_xpath = "//p[@id='notification-message' and contains(text(), 'Successfully delete workspace')]"
        result_element_after_delete = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, result_element_after_delete_xpath))
        )
        actual_result_after_delete = result_element_after_delete.text
        assert actual_result_after_delete == expected_result_after_delete, f"Expected: {expected_result_after_delete}, Actual: {actual_result_after_delete}"

        # Attach expected and actual results to the Allure report for Delete Workspace
        allure.attach(f"Expected Result - Delete Workspace: {expected_result_after_delete}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Delete Workspace: {actual_result_after_delete}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)

    def verify_workspace_details(self, driver, expected_name, expected_description):
        name_xpath = f"//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='{expected_name}']"
        description_xpath = f"//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='{expected_description}']"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, name_xpath + " | " + description_xpath))
        )

        workspace_name_element = driver.find_element(By.XPATH, name_xpath)
        actual_name = workspace_name_element.text
        assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"

        description_element = driver.find_element(By.XPATH, description_xpath)
        actual_description = description_element.text
        assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"

if __name__ == "__main__":
    pytest.main(["-s", "test_workspace_management.py"])
