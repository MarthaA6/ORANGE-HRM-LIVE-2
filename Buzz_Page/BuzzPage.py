import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Buzz_Locator.BuzzLocator import BuzzLocator


class BuzzPage:
    def __init__(self, driver):
        self.driver = driver

    def click_buzz_sidebar(self):
        click_buzz_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(BuzzLocator.BUZZ_SIDEBAR))
        click_buzz_sidebar.click()
        time.sleep(3)
