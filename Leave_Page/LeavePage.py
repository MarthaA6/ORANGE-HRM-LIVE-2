import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Leave_Locator.LeaveLocator import LeaveLocator


class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def click_leave_sidebar(self):
        click_leave_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.LEAVE_SIDEBAR))
        click_leave_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_apply_button(self):
        click_apply_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.APPLY_BUTTON))
        click_apply_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_my_leave_button(self):
        click_my_leave_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.MY_LEAVE_BUTTON))
        click_my_leave_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_employment_dropdown(self):
        click_employment_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.EMPLOYMENT_DROPDOWN))
        click_employment_dropdown.click()
        time.sleep(3)

    def click_add_entitlements_dropdown(self):
        click_add_entitlements_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.ADD_ENTITLEMENTS_DROPDOWN))
        click_add_entitlements_dropdown.click()
        time.sleep(3)

    def click_employee_entitlements_dropdown(self):
        click_employee_entitlements_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.EMPLOYEE_ENTITLEMENTS_DROPDOWN))
        click_employee_entitlements_dropdown.click()
        time.sleep(3)

    def click_my_entitlements_dropdown(self):
        click_my_entitlements_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.MY_ENTITLEMENTS_DROPDOWN))
        click_my_entitlements_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_reports_dropdown(self):
        click_reports_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.REPORTS_DROPDOWN))
        click_reports_dropdown.click()
        time.sleep(3)

    def click_leave_entitlements_and_usage_report_dropdown(self):
        click_leave_entitlements_and_usage_report_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.LEAVE_ENTITLEMENTS_AND_USAGE_REPORT_DROPDOWN))
        click_leave_entitlements_and_usage_report_dropdown.click()
        time.sleep(3)

    def click_my_leave_entitlements_and_usage_report_dropdown(self):
        click_my_leave_entitlements_and_usage_report_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT_DROPDOWN))
        click_my_leave_entitlements_and_usage_report_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_configure_dropdown(self):
        click_configure_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.CONFIGURE_DROPDOWN))
        click_configure_dropdown.click()
        time.sleep(3)

    def click_leave_period_dropdown(self):
        click_leave_period_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.LEAVE_PERIOD_DROPDOWN))
        click_leave_period_dropdown.click()
        time.sleep(3)

    def click_leave_types_dropdown(self):
        click_leave_types_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.LEAVE_TYPES_DROPDOWN))
        click_leave_types_dropdown.click()
        time.sleep(3)

    def click_work_week_dropdown(self):
        click_work_week_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.WORK_WEEK_DROPDOWN))
        click_work_week_dropdown.click()
        time.sleep(3)

    def click_holidays_dropdown(self):
        click_holidays_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.HOLIDAYS_DROPDOWN))
        click_holidays_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_leave_list_button(self):
        click_leave_list_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.LEAVE_LIST_BUTTON))
        click_leave_list_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_assign_leave_button(self):
        click_assign_leave_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocator.ASSIGN_LEAVE_BUTTON))
        click_assign_leave_button.click()
        time.sleep(3)

