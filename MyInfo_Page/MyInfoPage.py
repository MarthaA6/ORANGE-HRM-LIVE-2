import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from MyInfo_Locator.MyInfoLocator import MyInfoLocator


class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver

    def click_my_info_sidebar(self):
        click_my_info_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInfoLocator.MY_INFO_SIDEBAR))
        click_my_info_sidebar.click()
        time.sleep(3)
