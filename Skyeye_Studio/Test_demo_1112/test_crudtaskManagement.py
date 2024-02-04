
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class TestLogin:
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Positive Login Test")
    def test_login_positive(self):
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
        text_field.send_keys("TestWorkspace03")

        textarea_field = self.driver.find_element(By.XPATH, "//textarea[@name='description']")
        textarea_field.send_keys("TestTV")

        next_button = self.driver.find_element(By.XPATH,
                                          "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-19a5hzf']")
        next_button.click()



        # close_button_xpath = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium muiltr-ddsvio']"
        # close_button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
        # ActionChains(self.driver).move_to_element(close_button).click().perform()
        # time.sleep(2)

        # element_xpath = "//button[@class='MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root muiltr-4fdqqi']"
        # cancel_button = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        # ActionChains(self.driver).move_to_element(cancel_button).click().perform()
        #
        # time.sleep(2)
        wait = WebDriverWait(self.driver, 3)
        workspace_name = "TestWorkspace03"
        workspace_xpath = f"//span[contains(@class, 'MuiListItemText-primary') and text()='{workspace_name}']"
        workspace_button = wait.until(EC.element_to_be_clickable((By.XPATH, workspace_xpath)))
        workspace_button.click()


        button_xpath01 = "//button[@id='simple-tab-1']"
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath01)))
        button.click()

        button_xpath = "//button[@class='MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButtonBase-root muiltr-laoqdv']//p[contains(., 'Create New Project')]"
        button_element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button_element.click()

        input_xpath = "//input[@name='projectName' and @placeholder='Project Name']"
        input_field = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
        input_field.send_keys("TestProject03")

        select_xpath = "//div[@id='select' and @role='button']"
        select_element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, select_xpath)))
        select_element.click()


        element_xpath = "//body/div[@id='menu-province_id']/div[3]/ul[1]/li[1]"
        element01 = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element01.click()

        button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']"
        button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

        project_element_xpath = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary muiltr-bnbtnt' and text()='TestProject03']"
        project_element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, project_element_xpath)))
        project_element.click()


        button_xpath = "//button[contains(@class, 'MuiButtonBase-root') and contains(text(), 'Task List')]"
        button_element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button_element.click()

        element_xpath = "//p[text()='Create New Task']/ancestor::button"
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element.click()
        ## fill form create new task
        input_xpath = "//input[@name='taskName' and @placeholder='Name']"
        input_field = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
        input_field.send_keys("TestTask03")
        ## select province
        select_xpath = "//div[@id='select' and @role='button']"
        select_element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, select_xpath)))
        select_element.click()

        ### click type antenna
        menu_item_xpath = "//li[contains(@class, 'MuiMenuItem-root') and contains(text(), 'Guyed tower')]"
        menu_item_element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, menu_item_xpath)))
        menu_item_element.click()
        ## description
        description_input_xpath = "//input[@name='description' and @placeholder='Optional']"
        description_input = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, description_input_xpath)))
        description_input.send_keys("Testdemo")

        # Đường dẫn đến thư mục chứa các ảnh
        folder_path = "/home/ubuntu/imageTest/"
        image_files = [
            "tru1_1_00002.JPG",
            "tru1_1_00003.JPG",
            "tru1_1_00004.JPG",
            "tru1_1_00005.JPG",
            "tru1_1_00006.JPG"
        ]

        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)

            if os.path.isfile(image_path):
                # Find element input[type='file'] with id before uploaded image
                input_file = self.driver.find_element(By.ID, "myfiles")

                # Gửi đường dẫn của file vào phần tử input
                input_file.send_keys(image_path)

                # Thêm một thời gian ngủ nhỏ để đảm bảo file đã được tải lên trước khi tiếp tục
                time.sleep(1)
            else:
                print(f"File {image_file} does not exist or is not in the correct format.")
        time.sleep(1)
        # Xác định phần tử bạn muốn click (ví dụ: vị trí của ảnh trong element)
        element_xpath = "//div[contains(@class, 'leaflet-container')]"
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))

        # Lấy vị trí x, y trên phần tử (ở đây lấy giữa phần tử)
        x_offset = element.size['width'] / 2
        y_offset = element.size['height'] / 2


        # In ra giá trị x_offset và y_offset
        print(f"x_offset: {x_offset}, y_offset: {y_offset}")

        # Thực hiện cuộc gọi JavaScript Executor để thực hiện click
        self.driver.execute_script("arguments[0].click();", element)
        # Click on element Create
        button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']"
        button_element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        # Thực hiện hành động click
        button_element.click()
        ## Expected Result
        # Lấy danh sách tất cả các thông báo hiện có
        # Kiểm tra xem có thông báo nào có văn bản mong đợi hay không
        success_message_xpath = "//div[@class='MuiTypography-root MuiTypography-body1 muiltr-jw4c5p' and text()='Successfully create new task']"
        success_message = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath)))

        # Set the expected result
        expected_result = "Successfully create new task"

        # Print the expected result before checking the message
        print(f"Expected result: {expected_result}")

        # Check and print the actual result
        actual_result = success_message.text
        assert actual_result == expected_result, f"Message mismatch: Expected '{expected_result}', Received '{actual_result}'"
        print(f"Actual result: {actual_result}")


        # Maximum waiting time is set to 15 seconds (adjustable)
        wait = WebDriverWait(self.driver, 15)

        # Ensure that the task name "TestTask03" is displayed within 15 seconds
        task_name_xpath = "//span[contains(text(),'TestTask03')]"
        task_name_element = wait.until(EC.visibility_of_element_located((By.XPATH, task_name_xpath)))

        # Ensure that the name "GuyedTower" is displayed within 15 seconds on the taskManagement page
        guyed_tower_xpath = "//span[contains(text(),'GuyedTower')]"
        guyed_tower_element = wait.until(EC.visibility_of_element_located((By.XPATH, guyed_tower_xpath)))

        # Check and print the results
        assert task_name_element.text == "TestTask03", f"Task name doesn't match: {task_name_element.text}"
        print(f"Task name: {task_name_element.text}")

        assert guyed_tower_element.text == "GuyedTower", f"GuyedTower name doesn't match: {guyed_tower_element.text}"
        print(f"GuyedTower name: {guyed_tower_element.text}")
        ############
        wait = WebDriverWait(self.driver, 15)

        # Define the relative XPath
        button_xpath = "//tbody/tr[1]/td[7]/button[1]"

        # Wait until the button is clickable
        button_element = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        # Click on the button
        button_element.click()
        # Replace 'input_xpath' with the actual XPath of your input field
        input_xpath = "//input[@aria-invalid='false' and @placeholder='Name']"

        # Replace 'new_value' with the value you want to set
        new_value = "Update_TestTask03"

        # Wait for the input field to be present and visible
        input_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, input_xpath))
        )

        # Use JavaScript Executor to clear the value
        self.driver.execute_script("arguments[0].value = '';", input_element)

        # Send new keys to the input field
        input_element.send_keys(new_value)
        #########
        # Replace 'select_element_xpath' with the actual XPath of the element you want to click
        select_element_xpath = "//div[@id='select']"

        # Wait for the element to be clickable
        select_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, select_element_xpath))
        )

        # Click on the element
        select_element.click()

        element_xpath = "//body/div[@id='menu-']/div[3]/ul[1]/li[2]"

        # Wait for the element to be clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, element_xpath))
        )

        # Click on the element
        element.click()

        # Assuming you already have the driver instance

        # Replace 'textarea_xpath' with the actual XPath of the <textarea> element
        textarea_xpath = "//textarea[@placeholder='(Optional)']"

        # Wait for the textarea to be visible
        textarea = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, textarea_xpath))
        )

        # Clear existing value using BACK_SPACE key
        textarea.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

        # Send new value to the textarea
        new_value = "Update_Skyeye_Telecom"
        textarea.send_keys(new_value)
        button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-2el1n9']"

        # Wait for the button to be clickable
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )

        # Click on the button
        button.click()
        # Replace 'success_message_xpath' with the actual XPath of the success message
        success_message_xpath = "//div[contains(text(),'Successfully update task')]"

        # Wait for the success message to be visible
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )

        # Verify that the success message text is as expected
        expected_result = "Successfully update task"
        assert success_message.text == expected_result, f"Expected result does not match: {success_message.text}"

        # Print the expected result
        print(f"Expected result: {expected_result}")

        # Print the actual result
        print(f"Actual result: {success_message.text}")

        # Replace 'success_message_xpath' with the actual XPath of the success message
        # Replace 'success_message_xpath' with the actual XPath of the success message
        # Replace 'task_name_xpath' and 'tower_type_xpath' with the actual XPaths
        task_name_xpath = "//span[contains(text(),'Update_TestTask03')]"
        tower_type_xpath = "//span[contains(text(),'Monopole')]"

        # Wait for the updated task name to be visible on the task management page
        updated_task_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, task_name_xpath))
        )

        # Wait for the tower type to be visible on the task management page
        tower_type = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, tower_type_xpath))
        )

        # Verify the updated task name and tower type
        assert updated_task_name.text == "Update_TestTask03", f"Task name does not match: {updated_task_name.text}"
        assert tower_type.text == "Monopole", f"Tower type does not match: {tower_type.text}"

        # Print the results
        print(f"Updated task name: {updated_task_name.text}")
        print(f"Tower type: {tower_type.text}")
        # Replace 'delete_button_xpath' with the actual XPath of the delete button
        delete_button_xpath = "//tbody/tr[1]/td[7]/button[2]"

        # Wait for the delete button to be clickable
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )

        # Click the delete button
        delete_button.click()
        # Replace 'delete_span_xpath' with the actual XPath of the span containing 'Delete'
        delete_span_xpath = "//span[contains(text(),'Delete')]"

        # Wait for the delete span to be clickable
        delete_span = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_span_xpath))
        )

        # Click the delete span
        delete_span.click()
        # Replace 'delete_button_xpath' with the actual XPath of the delete button
        delete_button_xpath = "//button[contains(., 'Delete')]"

        # Wait for the delete button to be clickable
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )

        # Click the delete button
        delete_button.click()
        # Replace 'success_message_xpath' with the actual XPath of the success message
        success_message_xpath = "//div[contains(text(),'Successfully delete task')]"

        # Wait for the success message to be visible
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )

        # Verify that the success message text is as expected
        expected_result = "Successfully delete task"
        assert success_message.text == expected_result, f"Thông báo không khớp: {success_message.text}"

        # Print the expected result
        print(f"Expected result: {expected_result}")

        # Print the actual result
        print(f"Actual result: {success_message.text}")

        ########### Click task form
        xpath = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium muiltr-ddsvio']"

        # Chờ cho phần tử xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        # Click vào phần tử
        element.click()

        workspace_name = "TestWorkspace03"

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
        time.sleep(3)
        # Xác định element button
        # Chờ cho button xuất hiện trong vòng 10 giây (có thể điều chỉnh thời gian chờ tùy thuộc vào trang web của bạn)
        button_xpath = "//p[contains(text(),'Delete')]"
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        # Click vào button
        button.click()












