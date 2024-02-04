import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestWorkspaceManagement:
    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Create Workspace")
    def test_create_workspace(self, login_fixture):
        driver = login_fixture
        with allure.step("Create Workspace"):
        # Wait for the element to be visible
        element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

        # Click on the element to open the workspace creation form
        element = driver.find_element(By.XPATH, element_xpath)
        element.click()

        # Fill in the workspace creation form
        text_field = driver.find_element(By.XPATH, "//input[@name='name']")
        text_field.send_keys("TestWorkspace01")

        textarea_field = driver.find_element(By.XPATH, "//textarea[@name='description']")
        textarea_field.send_keys("Skyeye_Telecom")

        # Click on the "Next" button
        next_button_xpath = "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'muiltr-19a5hzf')]"
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        next_button.click()

        # Verify the success message
        expected_message = "Successfully add workspace TestWorkspace01"
        print(f"Expected result:{expected_message}" )
        # Wait for the success message
        success_message_xpath = "//p[@id='notification-message']"
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath)))
        actual_message = success_message.text
        print(f"Actudal result: {actual_message}")
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

        # Additional verification steps, if needed

        # Xpath của hai phần tử
        name_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='TestWorkspace01']"
        description_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Skyeye_Telecom']"

        # Chờ đến khi cả hai phần tử xuất hiện
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, name_xpath + " | " + description_xpath))
        )

        # Kiểm tra nội dung của phần tử tên workspace
        workspace_name_element = driver.find_element(By.XPATH, name_xpath)
        actual_name = workspace_name_element.text
        expected_name = "TestWorkspace01"
        assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"
        print(f"Workspace Name Element: {actual_name}")

        # Kiểm tra nội dung của phần tử mô tả workspace
        description_element = driver.find_element(By.XPATH, description_xpath)
        actual_description = description_element.text
        expected_description = "Skyeye_Telecom"
        assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"
        print(f"Description Element: {actual_description}")


    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Update Workspace")
    def test_update_workspace(self, login_fixture):
        driver = login_fixture
        with allure.step("Update Workspace"):

        # Edit workspace
        workspace_name = "TestWorkspace01"

        # Xác định xpath của span chứa tên workspace
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"

        # Chờ cho span xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        wait = WebDriverWait(driver, 10)
        workspace_span = wait.until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

        # Xác định xpath của button "Edit Workspace" tương ứng
        edit_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button"

        # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))

        # Click vào button "Edit Workspace"
        edit_button.click()
        # Xác định element input
        # Xác định element input và textarea
        input_element = driver.find_element(By.XPATH, "//input[@name='name' and @placeholder='Workspace Name']")

        # Chờ đến khi trường input và textarea xuất hiện
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))

        # Sử dụng Javascript Executor để xóa giá trị
        driver.execute_script("arguments[0].value = '';", input_element)



        # Gửi giá trị mới
        input_element.send_keys("Update_TestWorkspace01")
        textarea_element = driver.find_element(By.XPATH,
                                                    "//textarea[@name='description' and @placeholder='(Optional)']")

        # Sử dụng phím BACK_SPACE để xóa giá trịupda
        textarea_element.send_keys(Keys.CONTROL + "a")  # Chọn toàn bộ văn bản
        textarea_element.send_keys(Keys.BACKSPACE)  # Xóa văn bản đã chọn

        # Gửi giá trị mới
        textarea_element.send_keys("Update_Skyeye_Telecom")

        # Xác định element button
        button_element = driver.find_element(By.XPATH,
                                                  "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']")

        # Thực hiện click vào button
        button_element.click()

        # Kết quả mong đợi
        # Kết quả mong đợi sau khi edit
        # Kết quả mong đợi sau khi edit
        expected_result_after_edit = "Successfully update workspace"
        print(f"Expected result after edit: {expected_result_after_edit}")

        # Tìm element chứa kết quả sau khi edit
        result_element_after_edit_xpath = "//p[@id='notification-message' and contains(text(), 'Successfully update workspace')]"
        result_element_after_edit = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, result_element_after_edit_xpath))
        )

        # In ra kết quả thực tế sau khi edit
        actual_result_after_edit = result_element_after_edit.text
        print(f"Actual result after edit: {actual_result_after_edit}")

        # Kiểm tra và assert kết quả sau khi edit
        assert actual_result_after_edit == expected_result_after_edit, f"Expected: {expected_result_after_edit}, Actual: {actual_result_after_edit}"

        # Kiểm tra và assert
        ##
        # Chờ đến khi cả hai phần tử xuất hiện
        name_xpath_01 = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Update_TestWorkspace01']"
        description_xpath_01 = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Update_Skyeye_Telecom']"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, name_xpath_01 + " | " + description_xpath_01))
        )

        # Kiểm tra nội dung của phần tử tên workspace
        workspace_name_element = driver.find_element(By.XPATH, name_xpath_01)
        actual_name = workspace_name_element.text
        expected_name = "Update_TestWorkspace01"
        assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"
        print(f"Workspace Name Element: {actual_name}")

        # Kiểm tra nội dung của phần tử mô tả workspace
        description_element = driver.find_element(By.XPATH, description_xpath_01)
        actual_description = description_element.text
        expected_description = "Update_Skyeye_Telecom"
        assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"
        print(f"Description Element: {actual_description}")


    @pytest.mark.Skyeye_Studio
    @allure.feature("Workspace Management")
    @allure.title("Test Delete Workspace")
    def test_delete_workspace(self, login_fixture):
        driver = login_fixture
        with allure.step("Delete Workspace"):
        # Wait for the button to be clickable
        workspace_name = "Update_TestWorkspace01"
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"
        workspace_span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

        # Click on "Delete Workspace" button
        delete_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button[2]"
        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
        delete_button.click()

        # Confirm deletion
        delete_button_xpath = "//span[contains(text(),'Delete')]"
        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))
        delete_button.click()

        # Enter password
        password_input_xpath = "//input[@placeholder='Your password' and @type='password']"
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_input_xpath)))
        password_input.send_keys("Kentran212431302$")  # Replace with your actual password

        # Click on the final delete button
        button_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[5]/button[2]"
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

        # Wait for the success message after delete
        expected_result_after_delete = "Successfully delete workspace"
        print(f"Expected result after delete: {expected_result_after_delete}")
        result_element_after_delete_xpath = "//p[@id='notification-message' and contains(text(), 'Successfully delete workspace')]"
        result_element_after_delete = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, result_element_after_delete_xpath))
        )
        actual_result_after_delete = result_element_after_delete.text
        print(f"Actual result after delete: {actual_result_after_delete}")

        # Verify the success message after delete
        assert actual_result_after_delete == expected_result_after_delete, f"Expected: {expected_result_after_delete}, Actual: {actual_result_after_delete}"


