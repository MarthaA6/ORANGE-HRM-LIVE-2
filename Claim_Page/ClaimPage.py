import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Claim_Locator.ClaimLocator import ClaimLocator


class ClaimPage:
    def __init__(self, driver):
        self.driver = driver

    def click_claim_sidebar(self):
        click_claim_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.CLAIM_SIDEBAR))
        click_claim_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_configuration_dropdown(self):
        click_configuration_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.CONFIGURATION_DROPDOWN))
        click_configuration_dropdown.click()
        time.sleep(3)

    def events_dropdown(self):
        events_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.EVENTS_DROPDOWN))
        events_dropdown.click()
        time.sleep(3)

    def click_expense_types_dropdown(self):
        click_expense_types_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.EXPENSE_TYPES_DROPDOWN))
        click_expense_types_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_submit_claim_button(self):
        click_submit_claim_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.SUBMIT_CLAIM_BUTTON))
        click_submit_claim_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
    def my_claims_button(self):
        my_claims_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.MY_CLAIMS_BUTTON))
        my_claims_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
    def click_employee_claims_button(self):
        click_employee_claims_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.EMPLOYEE_CLAIMS_BUTTON))
        click_employee_claims_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_assign_claim_button(self):
        click_assign_claim_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocator.ASSIGN_CLAIM_BUTTON))
        click_assign_claim_button.click()
        time.sleep(3)

