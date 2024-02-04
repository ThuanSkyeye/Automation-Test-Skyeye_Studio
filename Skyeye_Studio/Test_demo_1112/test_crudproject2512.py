import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from test_login001 import login_fixture

class TestProjectManagement:
    def setup_method(self):
        self.workspace_name = ""

    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Create, Update, and Delete Project Management")
    def test_create_update_delete_projectManagement(self, login_fixture):
        driver = login_fixture

        # Step 1: Create Workspace
        with allure.step("Step 1: Create Workspace"):
            self.create_workspace(driver, "TestWorkspace02", "Skyeye_Telecom")

        # Step 2: Create Project
        with allure.step("Step 2: Create Project"):
            self.create_project(driver, "TestWorkspace02", "TestProject02", "Skyeye_Telecom")

        # Step 3: Update Project
        with allure.step("Step 3: Update Project"):
            self.update_project(driver, "TestWorkspace02", "TestProject02", "Update_TestProject02", "Update_Skyeye_Telecom")

        # Step 4: Delete Project
        with allure.step("Step 4: Delete Project"):
            self.delete_project(driver, "TestWorkspace02", "Update_TestProject02")

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

        # Attach expected and actual results to the Allure report for Create Workspace
        allure.attach(f"Expected Result - Create Workspace: {expected_message}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Create Workspace: {actual_message}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)

        # Additional verification steps, if needed

    def create_project(self, driver, workspace_name, project_name, project_description):
        # Chọn workspace đã tạo
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
        workspace_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))
        workspace_span.click()

        # Tạo project mới
        project_button_xpath = "//button[@id='simple-tab-1']"
        project_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, project_button_xpath)))
        project_button.click()

        new_project_button_xpath = "//p[contains(text(),'Create New Project')]"
        new_project_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, new_project_button_xpath)))
        new_project_button.click()

        project_name_input_xpath = "//input[@name='projectName' and @placeholder='Project Name']"
        project_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, project_name_input_xpath)))
        project_name_input.send_keys(project_name)

        select_xpath = "//div[@id='select' and @role='button']"
        select_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, select_xpath)))
        select_element.click()

        element_xpath = "//body/div[@id='menu-province_id']/div[3]/ul[1]/li[1]"
        element01 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element01.click()

        # Gửi giá trị vào trường textarea
        # Gửi giá trị vào trường textarea
        textarea_element = driver.find_element(By.XPATH,
                                               "//textarea[@name='description' and @placeholder='(Optional)']")
        textarea_element.send_keys(project_description)


        create_button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']"
        create_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, create_button_xpath)))
        create_button.click()

        expected_message = f"Create project {project_name} successfully"
        success_message_xpath = f"//p[@id='notification-message' and contains(text(), 'Create project {project_name} successfully')]"
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

        # Additional verification steps, if needed

        # Attach expected and actual results to the Allure report for Create Workspace
        allure.attach(f"Expected Result - Create Project: {expected_message}", name="Expected Result",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual Result - Create Project: {actual_message}", name="Actual Result",
                      attachment_type=allure.attachment_type.TEXT)

    def update_project(self, driver, workspace_name, old_project_name, updated_project_name, updated_project_description):
        # Chọn workspace và project cần cập nhật
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
        workspace_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))
        workspace_span.click()

        project_xpath = f"//span[contains(text(),'{old_project_name}')]"
        project_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, project_xpath)))
        project_span.click()

        # Click nút Edit
        edit_button_xpath = "//button[contains(text(),'Edit')]"
        edit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))
        edit_button.click()

        # Cập nhật thông tin project
        project_name_input_xpath = "//input[@name='name']"
        project_name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, project_name_input_xpath)))
        project_name_input.clear()
        project_name_input.send_keys(updated_project_name)

        project_description_input_xpath = "//textarea[@name='description']"
        project_description_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, project_description_input_xpath)))
        project_description_input.clear()
        project_description_input.send_keys(updated_project_description)

        # Click nút Save
        save_button_xpath = "//button[contains(text(),'Save')]"
        save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, save_button_xpath)))
        save_button.click()

        expected_message = "Successfully update project"
        success_message_xpath = "//p[@id='notification-message' and contains(text(),'Successfully update project')]"
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"


    def delete_project(self, driver, workspace_name, project_name):
        # Chọn workspace và project cần xóa
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
        workspace_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))
        workspace_span.click()

        project_xpath = f"//span[contains(text(),'{project_name}')]"
        project_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, project_xpath)))
        project_span.click()

        # Click nút Delete
        delete_button_xpath = "//button[contains(text(),'Delete')]"
        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
        delete_button.click()

        # Xác nhận xóa
        confirm_delete_button_xpath = "//span[contains(text(),'Delete')]"
        confirm_delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, confirm_delete_button_xpath)))
        confirm_delete_button.click()

        # Nhập mật khẩu và xác nhận
        password_input_xpath = "//input[@placeholder='Your password' and @type='password']"
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_input_xpath)))
        password_input.send_keys("YourPassword")  # Thay bằng mật khẩu thực tế

        confirm_button_xpath = "//button[contains(text(),'Confirm')]"
        confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, confirm_button_xpath)))
        confirm_button.click()

        expected_message = "Successfully delete project"
        success_message_xpath = "//p[@id='notification-message' and contains(text(),'Successfully delete project')]"
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"


if __name__ == "__main__":
    pytest.main(["-s", "test_project_management.py"])
