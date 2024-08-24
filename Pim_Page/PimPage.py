import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pim_Locator.PimLocator import PimLocator


class PimPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pim_sidebar(self):
        click_pim_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.PIM_SIDEBAR))
        click_pim_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_configuration_dropdown(self):
        click_configuration_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.CONFIGURATION_DROPDOWN))
        click_configuration_dropdown.click()
        time.sleep(3)

    def click_optional_fields_dropdown(self):
        click_optional_fields_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.OPTIONAL_FIELDS_DROPDOWN))
        click_optional_fields_dropdown.click()
        time.sleep(3)

    def click_custom_fields_dropdown(self):
        click_custom_fields_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.CUSTOM_FIELDS_DROPDOWN))
        click_custom_fields_dropdown.click()
        time.sleep(3)

    def click_data_import_dropdown(self):
        click_data_import_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.DATA_IMPORT_DROPDOWN))
        click_data_import_dropdown.click()
        time.sleep(3)

    def click_reporting_methods_dropdown(self):
        click_reporting_methods_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.REPORTING_METHODS_DROPDOWN))
        click_reporting_methods_dropdown.click()
        time.sleep(3)

    def click_termination_reasons_dropdown(self):
        click_termination_reasons_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.TERMINATION_REASONS_DROPDOWN))
        click_termination_reasons_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_employment_list_button(self):
        click_employment_list_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.EMPLOYMENT_LIST_BUTTON))
        click_employment_list_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_add_employee_button(self):
        click_add_employee_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.EMPLOYMENT_LIST_BUTTON))
        click_add_employee_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_reports_button(self):
        click_reports_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocator.REPORTS_BUTTON))
        click_reports_button.click()
        time.sleep(3)