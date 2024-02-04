import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def log_on_failure(request, driver=None):
    yield
    if driver and request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        try:
            driver = item.funcargs.get('driver', None)
            if driver:
                allure.attach(driver.get_screenshot_as_png(), "CreateWorkspace", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

@pytest.fixture
def login():
    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.25.185.68:10105/login")

    email = "vanthuancontact@gmail.com"
    password = "Kentran212431302&"

    # Login
    email_field = driver.find_element(By.XPATH, '//*[@name="email"]')
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, '//*[@name="password"]')
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    login_button.click()

    # Returning the driver object for testing
    yield driver

    # Teardown
    driver.quit()
