import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestWorkspaceManagement:
    def setup_method(self):
        self.created_workspace_name = ""
        self.updated_workspace_name = ""

    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Create Workspace")
    def test_create_workspace(self, login_fixture):
        driver = login_fixture
        with allure.step("Create Workspace"):
            element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

            element = driver.find_element(By.XPATH, element_xpath)
            element.click()

            text_field = driver.find_element(By.XPATH, "//input[@name='name']")
            text_field.send_keys("TestWorkspace01")

            textarea_field = driver.find_element(By.XPATH, "//textarea[@name='description']")
            textarea_field.send_keys("Skyeye_Telecom")

            next_button_xpath = "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'muiltr-19a5hzf')]"
            next_button = driver.find_element(By.XPATH, next_button_xpath)
            next_button.click()

            expected_message = "Successfully add workspace TestWorkspace01"
            success_message_xpath = "//p[@id='notification-message']"
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, success_message_xpath)))
            actual_message = success_message.text
            assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

            name_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='TestWorkspace01']"
            description_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Skyeye_Telecom']"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, name_xpath + " | " + description_xpath))
            )

            workspace_name_element = driver.find_element(By.XPATH, name_xpath)
            actual_name = workspace_name_element.text
            expected_name = "TestWorkspace01"
            assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"

            description_element = driver.find_element(By.XPATH, description_xpath)
            actual_description = description_element.text
            expected_description = "Skyeye_Telecom"
            assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"

            # Lưu lại tên workspace đã tạo
            self.created_workspace_name = expected_name

    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Update Workspace")
    def test_update_workspace(self, login_fixture):
        driver = login_fixture
        with allure.step("Update Workspace"):
            workspace_name = self.created_workspace_name
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

            input_element.send_keys("Update_TestWorkspace01")
            textarea_element = driver.find_element(By.XPATH, "//textarea[@name='description' and @placeholder='(Optional)']")
            textarea_element.send_keys(Keys.CONTROL + "a")
            textarea_element.send_keys(Keys.BACKSPACE)
            textarea_element.send_keys("Update_Skyeye_Telecom")

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

            name_xpath_01 = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Update_TestWorkspace01']"
            description_xpath_01 = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Update_Skyeye_Telecom']"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, name_xpath_01 + " | " + description_xpath_01))
            )

            workspace_name_element = driver.find_element(By.XPATH, name_xpath_01)
            actual_name = workspace_name_element.text
            expected_name = "Update_TestWorkspace01"
            assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"

            description_element = driver.find_element(By.XPATH, description_xpath_01)
            actual_description = description_element.text
            expected_description = "Update_Skyeye_Telecom"
            assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"

            # Lưu lại tên workspace đã cập nhật
            self.updated_workspace_name = expected_name

    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Delete Workspace")
    def test_delete_workspace(self, login_fixture):
        driver = login_fixture
        with allure.step("Delete Workspace"):
            workspace_name = self.updated_workspace_name
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
            password_input.send_keys("Kentran212431302$")  # Replace with your actual password

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
