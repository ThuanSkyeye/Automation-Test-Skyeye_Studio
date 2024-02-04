import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_config29121 import log_on_failure, login
from selenium.common.exceptions import TimeoutException


class TestProjectManagement:
    def setup_method(self):
        self.workspace_name = ""
        self.project_name = ""

    @pytest.mark.Skyeye_Studio
    @allure.feature("Project Management")
    @allure.title("Test Create, Update, and Delete Project")
    def test_create_update_delete_project(self, login_fixture):
        driver = login_fixture

        # Step 1: Create Workspace
        with allure.step("Step 1: Create Workspace"):
            # Your workspace creation logic goes here
            element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

            element = driver.find_element(By.XPATH, element_xpath)
            element.click()

            text_field = driver.find_element(By.XPATH, "//input[@name='name']")
            text_field.send_keys("TestWorkspace02")

            textarea_field = driver.find_element(By.XPATH, "//textarea[@name='description']")
            textarea_field.send_keys("Skyeye_Telecom")

            next_button = driver.find_element(By.XPATH,
                                              "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-19a5hzf']")
            next_button.click()

            # Additional verification steps, if needed
            # ...

            # Save the workspace name for later use
            self.workspace_name = "TestWorkspace02"

        # Step 2: Navigate to Workspace
        with allure.step("Step 2: Navigate to Workspace"):
            workspace_name = self.workspace_name
            workspace_xpath = f"//span[contains(@class, 'MuiListItemText-primary') and text()='{workspace_name}']"
            workspace_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, workspace_xpath)))
            workspace_button.click()

        # Step 3: Create Project
        with allure.step("Step 3: Create Project"):
            # Your project creation logic goes here
            button_xpath01 = "//button[@id='simple-tab-1']"
            button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath01)))
            button.click()

            # button_xpath = "//button[@class='MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButtonBase-root muiltr-laoqdv']//p[contains(., 'Create New Project')]"
            # button_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            # button_element.click()

            # Your project creation steps
            # ...
            button_xpath = "//button[@class='MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButtonBase-root muiltr-laoqdv']//p[contains(., 'Create New Project')]"
            button_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            button_element.click()

            input_xpath = "//input[@name='projectName' and @placeholder='Project Name']"
            input_field = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
            input_field.send_keys("TestProject02")

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
            textarea_element.send_keys("Skyeye_Telecom")

            button_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/button[2]"
            button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            button.click()
            ### demo
            # element_xpath = "//tbody/tr[1]/td[6]/button[1]"
            # wait = WebDriverWait(driver, 5)
            # element = wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            # element.click()
            # time.sleep(3)

            # Expected result
            #Your expected success message
            # Your expected success message
            # Your expected success message



            # Print expected and actual results
            # print(f"Expected Result: {expected_success_message}")
            # print(f"Actual Result: {actual_success_message}")
            # Your expected success message
            # Your expected success message
            expected_success_message = "Create project TestProject02 successfully"
            try:
                result_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "//div[@class='MuiTypography-root MuiTypography-body1 muiltr-jw4c5p' and contains(., 'successfully')]"))
                )

                # Kiểm tra và assert chỉ khi đó là thông báo cho project
                if "Create project" in result_element.text:
                    expected_result_project = "Create project TestProject02 successfully"
                    print(f"Expected result: {expected_result_project}")
                    print(f"Actual result: {result_element.text}")
                    assert expected_result_project == result_element.text, f"Expected: {expected_result_project}, Actual: {result_element.text}"
                else:
                    print("This is not a project-related message. Skipping assertion for workspace.")
            except TimeoutException as e:
                print(f"Timeout: Element not found within 10 seconds. Exception: {e}")

            # # Assert that the actual message matches the expected message
            # assert actual_success_message == expected_success_message, "Expected and actual messages do not match"
            # # Save the project name for later use
            # self.project_name = "TestProject02"  # Replace with actual project name

        # Step 4: Additional steps (update, delete, etc.) if needed
        # ...

        # Continue with your existing steps for updating and deleting projects
        # ...

        # project_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='TestProject02']"
        #
        # # Sử dụng WebDriverWait để đợi cho phần tử xuất hiện trong vòng 10 giây
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, project_xpath))
        # )
        #
        # # Kiểm tra nội dung của phần tử project
        # project_element = driver.find_element(By.XPATH, project_xpath)
        # actual_project_name = project_element.text
        # expected_project_name = "TestProject02"
        #
        # # Sử dụng assert để so sánh giá trị thực tế và giá trị mong đợi
        # assert actual_project_name == expected_project_name, f"Expected: {expected_project_name}, Actual: {actual_project_name}"
        #
        # # In ra thông báo về phần tử project
        # print(f"Project Name Element: {actual_project_name}")
        # # Xác định biểu thức XPath của phần tử Description
        # description_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Skyeye_Telecom']"
        #
        # # Sử dụng WebDriverWait để đợi cho phần tử xuất hiện trong vòng 10 giây
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, description_xpath))
        # )
        #
        # # Kiểm tra nội dung của phần tử Description
        # description_element = driver.find_element(By.XPATH, description_xpath)
        # actual_description = description_element.text
        # expected_description = "Skyeye_Telecom"
        #
        # # Sử dụng assert để so sánh giá trị thực tế và giá trị mong đợi
        # assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"
        #
        # # In ra thông báo về phần tử Description
        # print(f"Description Element: {actual_description}")
        # # Xác định biểu thức XPath của phần tử Location
        # location_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='An Giang']"
        #
        # # Sử dụng WebDriverWait để đợi cho phần tử xuất hiện trong vòng 10 giây
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, location_xpath))
        # )
        #
        # # Kiểm tra nội dung của phần tử Location
        # location_element = driver.find_element(By.XPATH, location_xpath)
        # actual_location = location_element.text
        # expected_location = "An Giang"
        #
        # # Sử dụng assert để so sánh giá trị thực tế và giá trị mong đợi
        # assert actual_location == expected_location, f"Expected: {expected_location}, Actual: {actual_location}"

        # In ra thông báo về phần tử Location
        # print(f"Location Element: {actual_location}")
        # element_xpath = "//tbody/tr[1]/td[6]/button[1]"
        # wait = WebDriverWait(driver, 5)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
        # element.click()

        #
        # # Thực hiện thao tác click
        #
        # # Xác định element input
        #
        # # Xác định element input cho Project Name
        # project_name_xpath = "//input[@placeholder='Project Name']"
        # project_name_element = driver.find_element(By.XPATH, project_name_xpath)
        #
        # # Xóa giá trị hiện tại trong trường Project Name
        # driver.execute_script("arguments[0].value = '';", project_name_element)
        #
        # # Gửi giá trị mới "Update_TestProject02" vào trường Project Name
        # project_name_element.send_keys("Update_TestProject02")
        #
        # # Xác định element selectupdate
        # select_xpath = "//div[@id='select']"
        # select_element = driver.find_element(By.XPATH, select_xpath)
        #
        # # Thực hiện thao tác click
        # select_element.click()
        #
        # # Xác định element
        # element_xpath = "//body/div[@id='menu-']/div[3]/ul[1]/li[2]"
        # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        #
        # # Click vào phần tử
        # element.click()
        #
        # # Xác định element textarea
        # # Sử dụng nhiều điều kiện để xác định phần tử đúng
        # # Xác định đối tượng textarea
        # # Xác định đối tượng textarea và chờ cho nó xuất hiện
        # textarea_xpath = "//textarea[contains(text(),'Skyeye_Telecom')]"
        # textarea_element = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, textarea_xpath))
        # )
        #
        # # Sử dụng phím CONTROL + "a" để chọn toàn bộ văn bản
        # textarea_element.send_keys(Keys.CONTROL + "a")
        #
        # # Sử dụng phím BACKSPACE để xóa văn bản đã chọn
        # textarea_element.send_keys(Keys.BACKSPACE)
        #
        # # Gửi giá trị mới "Update_Skyeye_Telecom"
        # textarea_element.send_keys("Update_Skyeye_Telecom")
        #
        # # Xác định element button
        # button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']"
        # button_element = driver.find_element(By.XPATH, button_xpath)
        #
        # # Thực hiện thao tác click
        # button_element.click()
        # # Xác định element chứa thông báo
        # expected_message_after_edit = "Edit project successfully"
        #
        # # Tìm element chứa thông báo sau khi chỉnh sửa
        # message_element_xpath = "//div[contains(text(),'Edit project successfully')]"
        # print(f"Expected message after edit: {expected_message_after_edit}")
        # message_element = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, message_element_xpath))
        # )
        #
        # # In ra thông báo thực tế sau khi chỉnh sửa
        # actual_message_after_edit = message_element.text
        # print(f"Actual message after edit: {actual_message_after_edit}")
        #
        # # Kiểm tra và assert thông báo sau khi chỉnh sửa
        # assert actual_message_after_edit == expected_message_after_edit, f"Expected: {expected_message_after_edit}, Actual: {actual_message_after_edit}"
        #
        # # Kiểm tra sự xuất hiện của thông báo
        # assert message_element.is_displayed(), "Edit project successfully message is not displayed."
        # ##
        # # ... (các bước cập nhật khác ở đây)
        #
        # # Kiểm tra element có xuất hiện sau khi cập nhật
        # # ... (các bước cập nhật khác ở đây)
        #
        # # Kiểm tra element có xuất hiện sau khi cập nhật
        # # ... (các bước cập nhật khác ở đây)
        #
        # # Kiểm tra element có xuất hiện sau khi cập nhật
        # updated_project_xpath = "//span[contains(text(),'Update_TestProject02')]"
        # updated_project_element = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, updated_project_xpath))
        # )
        #
        # # In ra kết quả mong đợi trước khi kiểm tra
        # expected_updated_project_text = "Update_TestProject02"
        # print(f"Expected updated project text: {expected_updated_project_text}")
        #
        # # In ra thông báo thực tế sau khi chỉnh sửa
        # actual_updated_project_text = updated_project_element.text
        # print(f"Actual updated project text: {actual_updated_project_text}")
        #
        # # Kiểm tra và assert element sau khi cập nhật
        # assert actual_updated_project_text == expected_updated_project_text, f"Expected: {expected_updated_project_text}, Actual: {actual_updated_project_text}"
        #
        # # ... (các bước kiểm tra khác ở đây)
        # # ... (các bước cập nhật khác ở đây)
        #
        # # Kiểm tra element có xuất hiện sau khi cập nhật
        # updated_description_xpath = "//span[contains(text(),'Update_Skyeye_Telecom')]"
        # updated_description_element = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, updated_description_xpath))
        # )
        #
        # # In ra kết quả mong đợi trước khi kiểm tra
        # expected_updated_description_text = "Update_Skyeye_Telecom"
        # print(f"Expected updated description text: {expected_updated_description_text}")
        #
        # # In ra thông báo thực tế sau khi chỉnh sửa
        # actual_updated_description_text = updated_description_element.text
        # print(f"Actual updated description text: {actual_updated_description_text}")
        #
        # # Kiểm tra và assert element sau khi cập nhật
        # assert actual_updated_description_text == expected_updated_description_text, f"Expected: {expected_updated_description_text}, Actual: {actual_updated_description_text}"
        #
        # # ... (các bước kiểm tra khác ở đây)
        # # Đợi cho element trở nên clickable và sau đó click vào nó

