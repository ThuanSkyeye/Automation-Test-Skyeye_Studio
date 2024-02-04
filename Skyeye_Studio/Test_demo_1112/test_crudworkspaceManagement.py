import time
import pytest
import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestWorkspaceManagement:
    @pytest.mark.Skyeye_Studio
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Positive Workspace Management Test")
    def test_create_workspace(self):
        # Gọi hàm đăng nhập từ TestLogin
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://172.25.254.0:10105/login")

        email_field = self.driver.find_element(By.XPATH, '//*[@name="email"]')
        email_field.send_keys("vanthuancontact@gmail.com")

        password_field = self.driver.find_element(By.XPATH, '//*[@name="password"]')
        password_field.send_keys("Kentran212431302$")

        login_button = self.driver.find_element(By.XPATH, '//*[@type="submit"]')
        login_button.click()

        element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

        text_field = self.driver.find_element(By.XPATH, "//input[@name='name']")
        text_field.send_keys("TestWorkspace01")

        textarea_field = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        textarea_field.send_keys("Skyeye_Telecom")

        next_button = self.driver.find_element(By.XPATH,
                                          "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-19a5hzf']")
        next_button.click()
        # Chờ đến khi thông báo xuất hiện
        # Chờ đến khi thông báo xuất hiện
        success_message_xpath = "//p[@id='add-workspace-notification' and contains(text(), 'Successfully add workspace TestWorkspace01')]"
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )

        # Kiểm tra nội dung của thông báo
        expected_message = "Successfully add workspace TestWorkspace01"
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"
        print(f"Expected message: {expected_message}, Actual message: {actual_message}")
        assert expected_message in actual_message, f"Expected: {expected_message}, Actual: {actual_message}"

        # Xpath của hai phần tử
        name_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='TestWorkspace01']"
        description_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Skyeye_Telecom']"

        # Chờ đến khi cả hai phần tử xuất hiện
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, name_xpath + " | " + description_xpath))
        )

        # Kiểm tra nội dung của phần tử tên workspace
        workspace_name_element = self.driver.find_element(By.XPATH, name_xpath)
        actual_name = workspace_name_element.text
        expected_name = "TestWorkspace01"
        assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"
        print(f"Workspace Name Element: {actual_name}")

        # Kiểm tra nội dung của phần tử mô tả workspace
        description_element = self.driver.find_element(By.XPATH, description_xpath)
        actual_description = description_element.text
        expected_description = "Skyeye_Telecom"
        assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"
        print(f"Description Element: {actual_description}")
        # Edit workspace
        # Xác định element
        workspace_name = "TestWorkspace01"

        # Xác định xpath của span chứa tên workspace
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"

        # Chờ cho span xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        wait = WebDriverWait(self.driver, 10)
        workspace_span = wait.until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

        # Xác định xpath của button "Edit Workspace" tương ứng
        edit_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button"

        # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))

        # Click vào button "Edit Workspace"
        edit_button.click()
        # Xác định element input
        # Xác định element input và textarea
        input_element = self.driver.find_element(By.XPATH, "//input[@name='name' and @placeholder='Workspace Name']")

        # Chờ đến khi trường input và textarea xuất hiện
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))

        # Sử dụng Javascript Executor để xóa giá trị
        self.driver.execute_script("arguments[0].value = '';", input_element)



        # Gửi giá trị mới
        input_element.send_keys("Update_TestWorkspace01")
        textarea_element = self.driver.find_element(By.XPATH,
                                                    "//textarea[@name='description' and @placeholder='(Optional)']")

        # Sử dụng phím BACK_SPACE để xóa giá trịupda
        textarea_element.send_keys(Keys.CONTROL + "a")  # Chọn toàn bộ văn bản
        textarea_element.send_keys(Keys.BACKSPACE)  # Xóa văn bản đã chọn

        # Gửi giá trị mới
        textarea_element.send_keys("Update_Skyeye_Telecom")

        # Xác định element button
        button_element = self.driver.find_element(By.XPATH,
                                                  "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']")

        # Thực hiện click vào button
        button_element.click()

        # Kết quả mong đợi
        # Kết quả mong đợi sau khi edit
        # Kết quả mong đợi sau khi edit
        expected_result_after_edit = "Successfully update workspace"

        # Tìm element chứa kết quả sau khi edit
        result_element_after_edit_xpath = "//p[@id='update-workspace-notification' and contains(text(), 'Successfully update workspace')]"
        result_element_after_edit = WebDriverWait(self.driver, 10).until(
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
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, name_xpath_01 + " | " + description_xpath_01))
        )

        # Kiểm tra nội dung của phần tử tên workspace
        workspace_name_element = self.driver.find_element(By.XPATH, name_xpath_01)
        actual_name = workspace_name_element.text
        expected_name = "Update_TestWorkspace01"
        assert actual_name == expected_name, f"Expected: {expected_name}, Actual: {actual_name}"
        print(f"Workspace Name Element: {actual_name}")

        # Kiểm tra nội dung của phần tử mô tả workspace
        description_element = self.driver.find_element(By.XPATH, description_xpath_01)
        actual_description = description_element.text
        expected_description = "Update_Skyeye_Telecom"
        assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"
        print(f"Description Element: {actual_description}")
        # Wait for the button to be clickable
        # Chờ cho đến khi đối tượng trở nên nhìn thấy (visible)
        # Xác định tên workspace cần xóa
        # Xác định tên workspace cần xóa
        workspace_name = "Update_TestWorkspace01"

        # Xác định xpath của span chứa tên workspace
        workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"

        # Chờ cho span xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        wait = WebDriverWait(self.driver, 10)
        workspace_span = wait.until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

        # Xác định xpath của button "Delete Workspace" tương ứng
        delete_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button[2]"

        # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))

        # Click vào button "Delete Workspace"
        delete_button.click()
        # Xác định element Delete
        delete_button_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Delete']"
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )

        # Thực hiện click vào element Delete
        delete_button.click()
        ###
        password_input_xpath = "//input[@placeholder='Your password' and @type='password']"
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, password_input_xpath))
        )

        # Gửi giá trị vào element input
        password_input.send_keys("Kentran212431302$")
        time.sleep(5)
        # Xác định element button
        # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ tùy thuộc vào trang web của bạn)
        button_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[4]/button[2]"
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        # Click vào button
        button.click()
        # Kết quả mong đợi sau khi xóa
        expected_result_after_delete = "Successfully delete workspace"

        # Tìm element chứa kết quả
        result_element_after_delete = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[@id='delete-workspace-notification' and contains(text(), 'Successfully delete workspace')]"))
        )

        # In ra kết quả thực tế sau khi xóa
        actual_result_after_delete = result_element_after_delete.text
        print(f"Actual result after delete: {actual_result_after_delete}")

        # Kiểm tra và assert sau khi xóa
        assert actual_result_after_delete == expected_result_after_delete, f"Expected: {expected_result_after_delete}, Actual: {actual_result_after_delete}"
        time.sleep(3)

        #



















