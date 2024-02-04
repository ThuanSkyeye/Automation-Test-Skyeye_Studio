from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import imaplib
import email
from email.header import decode_header


# Function to login to Gmail using Selenium
def login_to_gmail(email_address, password):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.gmail.com")

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    email_field.send_keys(email_address)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@id="identifierNext"]'))
    )
    next_button.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "Passwd"))
    )
    password_field.send_keys(password)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@id="passwordNext"]'))
    )
    next_button.click()

    # Add some waiting time to make sure the Gmail page is fully loaded
    time.sleep(5)

    return driver


# Function to login to Gmail using IMAP
def login_to_gmail_imap(email_address, password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, password)
        mail.select("inbox")
        return mail
    except Exception as e:
        print(f"IMAP login failed: {e}")
        return None


# Example usage
email_address = "qaautomationtest1001@gmail.com"
password = "Kentran212431302#"

# Login using Selenium
driver = login_to_gmail(email_address, password)

# If the login is successful using Selenium, proceed to login using IMAP
if driver:
    mail = login_to_gmail_imap(email_address, password)

    # Proceed with other actions using the 'driver' and 'mail' objects
    # ...

    # Close the Selenium driver
    driver.quit()

    # Close the IMAP connection
    if mail:
        mail.logout()
