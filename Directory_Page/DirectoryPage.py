import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Directory_Locator.DirectoryLocator import DirectoryLocator


class DirectoryPage:
    def __init__(self, driver):
        self.driver = driver

    def click_directory_sidebar(self):
        click_directory_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DirectoryLocator.DIRECTORY_SIDEBAR))
        click_directory_sidebar.click()
        time.sleep(3)
