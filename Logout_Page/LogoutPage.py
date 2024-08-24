import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Logout_Locator.LogoutLocator import LogoutLocator


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_user_dropdown(self):
        click_user_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocator.USER_DROPDOWN))
        click_user_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_logout_button(self):
        click_logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocator.LOGOUT_BUTTON))
        click_logout_button.click()
        time.sleep(3)
