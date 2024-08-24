import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Performance_Locator.PerformanceLocator import PerformanceLocator


class PerformancePage:
    def __init__(self, driver):
        self.driver = driver

    def click_performance_sidebar(self):
        click_performance_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.PERFORMANCE_SIDEBAR))
        click_performance_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_configure_dropdown(self):
        click_configure_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.CONFIGURE_DROPDOWN))
        click_configure_dropdown.click()
        time.sleep(3)

    def click_kpis_dropdown(self):
        click_kpis_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.KPIs_DROPDOWN))
        click_kpis_dropdown.click()
        time.sleep(3)

    def click_trackers_button(self):
        click_trackers_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.TRACKERS_DROPDOWN))
        click_trackers_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_manage_reviews_1_button(self):
        click_manage_reviews_1_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.MANAGE_REVIEWS_1_DROPDOWN))
        click_manage_reviews_1_button.click()
        time.sleep(3)

    def click_manage_reviews_2_button(self):
        click_manage_reviews_2_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.MANAGE_REVIEWS_2_DROPDOWN))
        click_manage_reviews_2_button.click()
        time.sleep(3)

    def click_my_reviews_dropdown(self):
        click_my_reviews_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.MY_REVIEWS_DROPDOWN))
        click_my_reviews_dropdown.click()
        time.sleep(3)

    def click_employee_reviews_dropdown(self):
        click_employee_reviews_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.EMPLOYEE_REVIEWS_DROPDOWN))
        click_employee_reviews_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_my_trackers_button(self):
        click_my_trackers_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.MY_TRACKERS_BUTTON))
        click_my_trackers_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_employee_trackers_button(self):
        click_employee_trackers_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocator.EMPLOYEE_TRACKERS_BUTTON))
        click_employee_trackers_button.click()
        time.sleep(3)