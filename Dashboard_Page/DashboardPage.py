import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Dashboard_Locator.DashboardLocator import DashboardLocator


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_dashboard_sidebar(self):
        click_dashboard_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashboardLocator.DASHBOARD_SIDEBAR))
        click_dashboard_sidebar.click()
        time.sleep(3)
