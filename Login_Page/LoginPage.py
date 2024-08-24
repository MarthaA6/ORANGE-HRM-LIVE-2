import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Login_Locator.LoginLocator import LoginLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, admin):
        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.USERNAME))
        username.send_keys(admin)
        time.sleep(5)

    def enter_password(self, admin123):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        password.send_keys(admin123)
        time.sleep(5)

    def click_login(self):
        login = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.LOGIN_BUTTON))
        login.click()
        time.sleep(5)
