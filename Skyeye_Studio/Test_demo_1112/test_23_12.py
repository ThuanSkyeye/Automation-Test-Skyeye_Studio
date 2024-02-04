import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from test_login001 import login_fixture
import time
from selenium.common.exceptions import NoSuchElementException

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
            element_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap muiltr-nhc4uc']"
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath))).click()
            text_field = driver.find_element(By.XPATH, "//input[@name='name']")
            text_field.send_keys("TestWorkspace02")
            textarea_field = driver.find_element(By.XPATH, "//textarea[@name='description']")
            textarea_field.send_keys("Skyeye_Telecom")
            next_button = driver.find_element(By.XPATH,
                                              "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-19a5hzf']")
            next_button.click()
            self.workspace_name = "TestWorkspace02"

        # Step 2: Navigate to Workspace
        with allure.step("Step 2: Navigate to Workspace"):
            workspace_name = self.workspace_name
            workspace_xpath = f"//span[contains(@class, 'MuiListItemText-primary') and text()='{workspace_name}']"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, workspace_xpath))).click()

        # Step 3: Create Project
        with allure.step("Step 3: Create Project"):
            button_xpath01 = "//button[@id='simple-tab-1']"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath01))).click()

            button_xpath = "//button[@class='MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButtonBase-root muiltr-laoqdv']//p[contains(., 'Create New Project')]"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()

            input_xpath = "//input[@name='projectName' and @placeholder='Project Name']"
            input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
            input_field.send_keys("TestProject02")

            select_xpath = "//div[@id='select' and @role='button']"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, select_xpath))).click()

            element_xpath = "//body/div[@id='menu-province_id']/div[3]/ul[1]/li[1]"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()

            textarea_element = driver.find_element(By.XPATH,
                                                   "//textarea[@name='description' and @placeholder='(Optional)']")
            textarea_element.send_keys("Skyeye_Telecom")

            button_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/button[2]"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()

            # Extended wait time for the notification element
            # Additional verification steps, if needed
            # Additional verification steps
            try:
                result_element = WebDriverWait(driver, 10).until(
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

            # Xác định biểu thức XPath của phần tử project trong quản lý dự án
            project_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='TestProject02']"

            # Sử dụng WebDriverWait để đợi cho phần tử xuất hiện trong vòng 10 giây
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, project_xpath))
            )

            # Kiểm tra nội dung của phần tử project
            project_element = driver.find_element(By.XPATH, project_xpath)
            actual_project_name = project_element.text
            expected_project_name = "TestProject02"

            # Sử dụng assert để so sánh giá trị thực tế và giá trị mong đợi
            assert actual_project_name == expected_project_name, f"Expected: {expected_project_name}, Actual: {actual_project_name}"

            # In ra thông báo về phần tử project
            print(f"Project Name Element: {actual_project_name}")
            # Xác định biểu thức XPath của phần tử Description
            description_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Skyeye_Telecom']"

            # Sử dụng WebDriverWait để đợi cho phần tử xuất hiện trong vòng 10 giây
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, description_xpath))
            )

            # Kiểm tra nội dung của phần tử Description
            description_element = driver.find_element(By.XPATH, description_xpath)
            actual_description = description_element.text
            expected_description = "Skyeye_Telecom"

            # Sử dụng assert để so sánh giá trị thực tế và giá trị mong đợi
            assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"

            # In ra thông báo về phần tử Description
            print(f"Description Element: {actual_description}")
            # Xác định biểu thức XPath của phần tử Location
            location_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='An Giang']"

            # Sử dụng WebDriverWait để đợi cho phần tử xuất hiện trong vòng 10 giây
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, location_xpath))
            )

            # Kiểm tra nội dung của phần tử Location
            location_element = driver.find_element(By.XPATH, location_xpath)
            actual_location = location_element.text
            expected_location = "An Giang"

            # Sử dụng assert để so sánh giá trị thực tế và giá trị mong đợi
            assert actual_location == expected_location, f"Expected: {expected_location}, Actual: {actual_location}"

            # In ra thông báo về phần tử Location
            print(f"Location Element: {actual_location}")
            # Chờ cho phần tử xuất hiện trước khi thực hiện thao tác
            # Chờ và click vào phần tử
            # Xác định element button
            # Xác định element button
            # button_xpath = "//tbody/tr[1]/td[7]/button[1]"
            # button_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            #
            # # Thực hiện thao tác click
            # button_element.click()
            # Xác định element button
            # Xác định element button
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//tbody/tr[1]/td[6]/button[1]"))
            )

            # Thực hiện hành động click
            element.click()

            # Thực hiện thao tác click

            # Xác định element input

            # Xác định element input cho Project Name
            project_name_xpath = "//input[@placeholder='Project Name']"
            project_name_element = self.driver.find_element(By.XPATH, project_name_xpath)

            # Xóa giá trị hiện tại trong trường Project Name
            self.driver.execute_script("arguments[0].value = '';", project_name_element)

            # Gửi giá trị mới "Update_TestProject02" vào trường Project Name
            project_name_element.send_keys("Update_TestProject02")

            # Xác định element selectupdate
            select_xpath = "//div[@id='select']"
            select_element = self.driver.find_element(By.XPATH, select_xpath)

            # Thực hiện thao tác click
            select_element.click()

            # Xác định element
            element_xpath = "//body/div[@id='menu-']/div[3]/ul[1]/li[2]"
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))

            # Click vào phần tử
            element.click()

            # Xác định element textarea
            # Sử dụng nhiều điều kiện để xác định phần tử đúng
            # Xác định đối tượng textarea
            # Xác định đối tượng textarea và chờ cho nó xuất hiện
            textarea_xpath = "//textarea[contains(text(),'Skyeye_Telecom')]"
            textarea_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, textarea_xpath))
            )

            # Sử dụng phím CONTROL + "a" để chọn toàn bộ văn bản
            textarea_element.send_keys(Keys.CONTROL + "a")

            # Sử dụng phím BACKSPACE để xóa văn bản đã chọn
            textarea_element.send_keys(Keys.BACKSPACE)

            # Gửi giá trị mới "Update_Skyeye_Telecom"
            textarea_element.send_keys("Update_Skyeye_Telecom")

            # Xác định element button
            button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']"
            button_element = self.driver.find_element(By.XPATH, button_xpath)

            # Thực hiện thao tác click
            button_element.click()
            # Xác định element chứa thông báo
            expected_message_after_edit = "Edit project successfully"

            # Tìm element chứa thông báo sau khi chỉnh sửa
            message_element_xpath = "//div[contains(text(),'Edit project successfully')]"
            print(f"Expected message after edit: {expected_message_after_edit}")
            message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, message_element_xpath))
            )

            # In ra thông báo thực tế sau khi chỉnh sửa
            actual_message_after_edit = message_element.text
            print(f"Actual message after edit: {actual_message_after_edit}")

            # Kiểm tra và assert thông báo sau khi chỉnh sửa
            assert actual_message_after_edit == expected_message_after_edit, f"Expected: {expected_message_after_edit}, Actual: {actual_message_after_edit}"

            # Kiểm tra sự xuất hiện của thông báo
            assert message_element.is_displayed(), "Edit project successfully message is not displayed."
            ##
            # ... (các bước cập nhật khác ở đây)

            # Kiểm tra element có xuất hiện sau khi cập nhật
            # ... (các bước cập nhật khác ở đây)

            # Kiểm tra element có xuất hiện sau khi cập nhật
            # ... (các bước cập nhật khác ở đây)

            # Kiểm tra element có xuất hiện sau khi cập nhật
            updated_project_xpath = "//span[contains(text(),'Update_TestProject02')]"
            updated_project_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, updated_project_xpath))
            )

            # In ra kết quả mong đợi trước khi kiểm tra
            expected_updated_project_text = "Update_TestProject02"
            print(f"Expected updated project text: {expected_updated_project_text}")

            # In ra thông báo thực tế sau khi chỉnh sửa
            actual_updated_project_text = updated_project_element.text
            print(f"Actual updated project text: {actual_updated_project_text}")

            # Kiểm tra và assert element sau khi cập nhật
            assert actual_updated_project_text == expected_updated_project_text, f"Expected: {expected_updated_project_text}, Actual: {actual_updated_project_text}"

            # ... (các bước kiểm tra khác ở đây)
            # ... (các bước cập nhật khác ở đây)

            # Kiểm tra element có xuất hiện sau khi cập nhật
            updated_description_xpath = "//span[contains(text(),'Update_Skyeye_Telecom')]"
            updated_description_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, updated_description_xpath))
            )

            # In ra kết quả mong đợi trước khi kiểm tra
            expected_updated_description_text = "Update_Skyeye_Telecom"
            print(f"Expected updated description text: {expected_updated_description_text}")

            # In ra thông báo thực tế sau khi chỉnh sửa
            actual_updated_description_text = updated_description_element.text
            print(f"Actual updated description text: {actual_updated_description_text}")

            # Kiểm tra và assert element sau khi cập nhật
            assert actual_updated_description_text == expected_updated_description_text, f"Expected: {expected_updated_description_text}, Actual: {actual_updated_description_text}"

            # ... (các bước kiểm tra khác ở đây)
            # Đợi cho element trở nên clickable và sau đó click vào nó
            button_xpath = "//tbody/tr[1]/td[6]/button[2]"
            button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            button_element.click()
            # Đợi cho element trở nên clickable và sau đó click vào nó
            element_xpath = "//body/div[2]/div[3]/div[1]/ul[1]/li[1]/div[1]"
            element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
            element.click()
            # Đợi cho element trở nên hiển thị
            # Đợi cho element trở nên hiển thị
            password_input_xpath = "//input[@type='password' and @placeholder='Your password']"
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, password_input_xpath)))

            # Gửi giá trị vào ô input
            password_input.send_keys("Kentran212431302$")
            # Đợi cho element trở nên hiển thị
            button_xpath = '//body/div[2]/div[3]/div[1]/div[1]/div[4]/button[2]'
            button_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

            # Thực hiện thao tác click
            button_element.click()
            # Xác định thông báo sau khi xóa thành công
            success_message_xpath = "//div[contains(text(),'Successfully delete your project')]"

            # Lấy văn bản mong đợi của thông báo
            expected_success_message = "Successfully delete your project"
            print(f"Expected success message: {expected_success_message}")

            # Chờ đợi để xác nhận thông báo xuất hiện trong vòng 20 giây
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, success_message_xpath)))

            # Lấy văn bản thực tế của thông báo
            actual_success_message = success_message.text
            print(f"Actual success message: {actual_success_message}")

            # Kiểm tra và assert thông báo sau khi xóa thành công
            assert actual_success_message == expected_success_message, f"Expected: {expected_success_message}, Actual: {actual_success_message}"

            # Kiểm tra sự xuất hiện của thông báo
            # Định nghĩa xpath của button
            # Định nghĩa xpath của button
            # Định nghĩa xpath của element
            element_xpath = "//body/div[@id='root']/div[@id='fuse-layout']/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/*[1]"
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))
            )

            # Thực hiện thao tác click
            element.click()
            # Chờ cho đến khi đối tượng trở nên nhìn thấy (visible)
            workspace_name = "TestWorkspace02"

            # Xác định xpath của span chứa tên workspace
            workspace_xpath = f"//span[contains(text(),'{workspace_name}')]"

            # Chờ cho span xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
            wait = WebDriverWait(driver, 10)
            workspace_span = wait.until(EC.presence_of_element_located((By.XPATH, workspace_xpath)))

            # Xác định xpath của button "Delete Workspace" tương ứng
            delete_button_xpath = f"{workspace_xpath}/ancestor::td/following-sibling::td/button[2]"

            # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
            delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))

            # Click vào button "Delete Workspace"
            delete_button.click()
            # Xác định element Delete
            delete_button_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='Delete']"
            delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
            )

            # Thực hiện click vào element Delete
            delete_button.click()
            # Thực hiện thao tác click
            password_input_xpath = "//input[@type='password' and @placeholder='Your password']"
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, password_input_xpath)))

            # Gửi giá trị vào ô input
            password_input.send_keys("Kentran212431302$")

            # Xác định element Delet
            ###
            # Xác định đối tượng WebElement của ô nhập liệu

            # Xác định element button

            # Xác định xpath của button "Delete"
            delete_button_xpath = "//p[contains(text(),'Delete')]"

            # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
            wait = WebDriverWait(driver, 10)
            delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, delete_button_xpath)))

            # Click vào button "Delete"
            delete_button.click()
            # Định nghĩa xpath của element


