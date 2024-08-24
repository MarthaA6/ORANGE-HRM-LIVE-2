import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Time_Locator.TimeLocator import TimeLocator


class TimePage:
    def __init__(self, driver):
        self.driver = driver

    def click_time_sidebar(self):
        click_time_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.TIME_SIDEBAR))
        click_time_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_time_sheets_dropdown(self):
        click_time_sheets_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.TIME_SHEETS_DROPDOWN))
        click_time_sheets_dropdown.click()
        time.sleep(3)

    def click_my_time_sheets_dropdown(self):
        click_my_time_sheets_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.MY_TIME_SHEETS_DROPDOWN))
        click_my_time_sheets_dropdown.click()
        time.sleep(3)

    def click_employee_time_sheets_dropdown(self):
        click_employee_time_sheets_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.EMPLOYEE_TIME_SHEETS_DROPDOWN))
        click_employee_time_sheets_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_attendance_dropdown(self):
        click_attendance_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.ATTENDANCE_DROPDOWN))
        click_attendance_dropdown.click()
        time.sleep(3)

    def click_my_records_dropdown(self):
        click_my_records_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.PUNCH_IN_OUT_DROPDOWN))
        click_my_records_dropdown.click()
        time.sleep(3)

    def click_punch_in_out_dropdown(self):
        click_punch_in_out_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.PUNCH_IN_OUT_DROPDOWN))
        click_punch_in_out_dropdown.click()
        time.sleep(3)

    def click_employee_records_dropdown(self):
        click_employee_records_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.EMPLOYEE_RECORDS_DROPDOWN))
        click_employee_records_dropdown.click()
        time.sleep(3)

    def click_configuration_dropdown(self):
        click_configuration_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.CONFIGURATION_DROPDOWN))
        click_configuration_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_reports_dropdown(self):
        click_reports_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.REPORTS_DROPDOWN))
        click_reports_dropdown.click()
        time.sleep(3)

    def click_projects_reports_dropdown(self):
        click_projects_reports_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.PROJECT_REPORTS_DROPDOWN))
        click_projects_reports_dropdown.click()
        time.sleep(3)

    def click_employee_reports_dropdown(self):
        click_employee_reports_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.EMPLOYEE_REPORTS_DROPDOWN))
        click_employee_reports_dropdown.click()
        time.sleep(3)

    def click_advance_summary_dropdown(self):
        click_advance_summary_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.ADVANCE_SUMMARY_DROPDOWN))
        click_advance_summary_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_project_info_dropdown(self):
        click_project_info_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.PROJECT_INFO_DROPDOWN))
        click_project_info_dropdown.click()
        time.sleep(3)

    def click_customers_dropdown(self):
        click_customers_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.CUSTOMERS_DROPDOWN))
        click_customers_dropdown.click()
        time.sleep(3)

    def click_projects_dropdown(self):
        click_projects_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeLocator.PROJECTS_DROPDOWN))
        click_projects_dropdown.click()
        time.sleep(3)
