import pytest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.fixture(scope="function")
def login(request):
    # Thực hiện logic đăng nhập của bạn ở đây và trả về đối tượng WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.25.185.68:10105/login")

    email_field = driver.find_element(By.XPATH, '//*[@name="email"]')
    email_field.send_keys("vanthuancontact@gmail.com")

    password_field = driver.find_element(By.XPATH, '//*[@name="password"]')
    password_field.send_keys("Kentran212431302&")

    login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    login_button.click()
    # Thực hiện các hành động đăng nhập
    yield driver  # Trả về đối tượng driver cho kiểm thử
    driver.quit()  # Dọn dẹp sau khi kiểm thử kết thúc


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def log_on_failure(request):
    msgs = []
    yield msgs.append
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)

