import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Skyeye_Studio.Test_demo_1112.test_login import TestLogin

class TestWorkspaceManagement01(TestLogin):
    def __init__(self):
        self.driver = None

    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Positive Workspace Management Test")
    def test_create_workspace(self, login_fixture, driver):  # Thêm login_fixture làm tham số
        # Thay đổi ở đây: Sử dụng login_fixture để có self.driver
        login_fixture()

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

        # Add any additional workspace verification steps here if needed

    # Không cần teardown_method nếu bạn muốn giữ trạng thái đăng nhập giữa các testcase

if __name__ == "__main__":
    pytest.main()
