import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Maintenance_Locator.MaintenanceLocator import MaintenanceLocator


class MaintenancePage:
    def __init__(self, driver):
        self.driver = driver

    def click_maintenance_sidebar(self):
        click_maintenance_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.MAINTENANCE_SIDEBAR))
        click_maintenance_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# ADMINISTRATOR_ACCESS
    def enter_password(self, admin123):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.PASSWORD))
        enter_password.send_keys(admin123)
        time.sleep(5)

    def click_confirm_button(self):
        click_confirm_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.CONFIRM_BUTTON))
        click_confirm_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_purge_records_dropdown(self):
        click_purge_records_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.PURGE_RECORDS_DROPDOWN))
        click_purge_records_dropdown.click()
        time.sleep(3)

    def click_employee_records_dropdown(self):
        click_employee_records_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.EMPLOYEE_RECORDS_DROPDOWN))
        click_employee_records_dropdown.click()
        time.sleep(3)

    def click_candidate_records_dropdown(self):
        click_candidate_records_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.CANDIDATE_RECORDS_DROPDOWN))
        click_candidate_records_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_access_records_button(self):
        click_access_records_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocator.ACCESS_RECORDS_BUTTON))
        click_access_records_button.click()
        time.sleep(3)
