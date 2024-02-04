
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Test_member:
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
        # Replace 'element_xpath' with the actual XPath of the element
        # Xpath của element cần click
        # Xpath của element cần click
        # Xpath của element cần click
        element_xpath = "//span[contains(text(),'Member')]"

        # Đợi cho element xuất hiện và clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, element_xpath))
        )

        # Thực hiện click
        element.click()
        # Replace 'element_xpath' with the actual XPath of the element
        element_xpath = "//button[contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'muiltr-1p5micz')]"

        # Click on the element
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, element_xpath))
        )
        element.click()
        # Replace 'element_xpath' with the actual XPath of the element
        element_xpath = "//input[@name='email' and @placeholder='Email']"

        # Find the input element
        input_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, element_xpath))
        )

        # Clear existing value and send keys
        input_element.send_keys("test0612@guysmail.com")
        # Replace 'button_xpath' with the actual XPath of the button
        button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-1lbycoa']"

        # Find and click the button
        invite_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        invite_button.click()
        # Replace 'success_message_xpath' with the actual XPath of the success message
        success_message_xpath = "//p[@id='notification-message']"


        # Wait for the success message to be visible
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )

        # Verify that the success message text is as expected
        expected_result = "Successfully invite member"
        assert success_message.text == expected_result, f"Notifications do not match: {success_message.text}"

        # Print the results
        print(f"Expected result: {expected_result}")
        print(f"Actual result: {success_message.text}")
        # Replace 'email_xpath', 'status_xpath', and 'role_xpath' with the actual XPaths
        email_xpath = "//span[contains(text(),'test0612@guysmail.com')]"
        status_xpath = "//span[@class='MuiChip-label MuiChip-labelMedium muiltr-9iedg7' and contains(text(),'Pending')]"
        role_xpath = "//span[@class='ant-select-selection-item' and contains(text(),'Member')]"

        # Wait for the email, status, and role elements to be visible on the member table
        email_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, email_xpath))
        )
        status_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, status_xpath))
        )
        role_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, role_xpath))
        )

        # Verify the email, status, and role
        assert email_element.text == "test0612@guysmail.com", f"Email does not match: {email_element.text}"
        assert status_element.text == "Pending", f"Status does not match: {status_element.text}"
        assert role_element.text == "Member", f"Role does not match: {role_element.text}"

        # Print the results
        print(f"Email: {email_element.text}")
        print(f"Status: {status_element.text}")
        print(f"Role: {role_element.text}")


        # Replace 'email_to_delete' with the actual email you want to delete
        email_to_delete = "test0612@guysmail.com"

        # Xpath to find the row containing the specified email
        row_xpath = f"//tbody/tr[.//span[contains(text(),'{email_to_delete}')]]"

        # Wait for the row to be visible
        row_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, row_xpath))
        )

        # Xpath to find the delete button within the row
        delete_button_xpath = f"{row_xpath}/td[8]/button[1]"

        # Wait for the delete button to be clickable
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )

        # Click the delete button
        delete_button.click()
        # Xpath của button Delete
        delete_button_xpath = "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root muiltr-17eolyq']"

        # Đợi cho button Delete trở nên clickable
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )

        # Click vào button Delete
        delete_button.click()
        # # Xpath của thông báo thành công sau khi xóa
        # # Replace 'success_message_xpath' with your actual XPath
        # # Replace 'success_message_xpath' with your actual XPath
        # # Kiểm tra sự xuất hiện của phần tử sau khi xóa
        # # Kiểm tra sự xuất hiện của phần tử sau khi xóa
        # # Thực hiện các bước để mời thành viên, giống như trong test_login_positive
        #
        # # Thêm bước kiểm tra mời thành viên thành công ở đây
        #
        # # Thực hiện bước xóa thành viên
        # # Kiểm tra sự xuất hiện của phần tử sau khi xóa
        # # Kiểm tra thông báo xóa thành viên
        # # Replace 'delete_success_message_xpath' with the actual XPath of the success message after deleting
        # # delete_success_message_xpath = "//div[@data-type='delete-success']"
        # #
        # # # Wait for the success message after deleting to be visible
        # # delete_success_message = WebDriverWait(self.driver, 10).until(
        # #     EC.visibility_of_element_located((By.XPATH, delete_success_message_xpath))
        # # )
        # #
        # # # Verify that the success message after deleting is as expected
        # # expected_delete_result = "Successfully delete member"
        # # assert delete_success_message.text == expected_delete_result, f"Xóa thành viên: Thông báo không khớp: {delete_success_message.text}"
        # #
        # # # Print the success message after deleting
        # # print(f"Expected result after deleting: {expected_delete_result}")
        # # Wait for the element with the expected text to be present in the DOM
        # Chờ đến khi thông báo xuất hiện
        success_message_xpath = "//p[@id='notification-message']"
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )

        # Kiểm tra nội dung của thông báo
        expected_message = "Successfully delete member"
        actual_message = success_message.text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"
        # Print the results
        print(f"Expected result: {expected_result}")
        print(f"Actual result: {success_message.text}")



























