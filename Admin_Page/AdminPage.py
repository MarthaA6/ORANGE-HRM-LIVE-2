import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Admin_Locator.AdminLocator import AdminLocator


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_sidebar(self):
        click_admin_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.ADMIN_SIDEBAR))
        click_admin_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_user_management_dropdown(self):
        click_user_management_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.USER_MANAGEMENT_DROPDOWN))
        click_user_management_dropdown.click()
        time.sleep(3)

    def click_users_dropdown(self):
        click_users_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.USERS_DROPDOWN))
        click_users_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_job_dropdown(self):
        click_job_dropdown_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.JOB_DROPDOWN))
        click_job_dropdown_dropdown.click()
        time.sleep(3)

    def click_job_titles_dropdown(self):
        click_job_titles_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.JOB_TITLES_DROPDOWN))
        click_job_titles_dropdown.click()
        time.sleep(3)

    def click_pay_grades_dropdown(self):
        click_pay_grades_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.PAY_GRADES_DROPDOWN))
        click_pay_grades_dropdown.click()
        time.sleep(3)

    def click_employment_status_dropdown(self):
        click_employment_status_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.EMPLOYMENT_STATUS_DROPDOWN))
        click_employment_status_dropdown.click()
        time.sleep(3)

    def click_job_categories_dropdown(self):
        click_job_categories_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.JOB_CATEGORIES_DROPDOWN))
        click_job_categories_dropdown.click()
        time.sleep(3)

    def click_work_shifts_dropdown(self):
        click_work_shifts_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.WORK_SHIFTS_DROPDOWN))
        click_work_shifts_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_organization_dropdown(self):
        click_organization_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.ORGANIZATION_DROPDOWN))
        click_organization_dropdown.click()
        time.sleep(3)

    def click_general_information_dropdown(self):
        click_general_information_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.GENERAL_INFORMATION_DROPDOWN))
        click_general_information_dropdown.click()
        time.sleep(3)

    def click_locations_dropdown(self):
        click_locations_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.LOCATIONS_DROPDOWN))
        click_locations_dropdown.click()
        time.sleep(3)

    def click_structure_dropdown(self):
        click_structure_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.STRUCTURE_DROPDOWN))
        click_structure_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_qualifications_dropdown(self):
        click_qualifications_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.QUALIFICATIONS_DROPDOWN))
        click_qualifications_dropdown.click()
        time.sleep(3)

    def click_skills_dropdown(self):
        click_skills_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.SKILLS_DROPDOWN))
        click_skills_dropdown.click()
        time.sleep(3)

    def click_education_dropdown(self):
        click_education_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.EDUCATION_DROPDOWN))
        click_education_dropdown.click()
        time.sleep(3)

    def click_licenses_dropdown(self):
        click_licenses_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.LICENSES_DROPDOWN))
        click_licenses_dropdown.click()
        time.sleep(3)

    def click_languages_dropdown(self):
        click_languages_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.LANGUAGES_DROPDOWN))
        click_languages_dropdown.click()
        time.sleep(3)

    def click_memberships_dropdown(self):
        click_memberships_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.MEMBERSHIPS_DROPDOWN))
        click_memberships_dropdown.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_nationalities_button(self):
        click_nationalities_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.NATIONALITIES_BUTTON))
        click_nationalities_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_corporate_branding_button(self):
        click_corporate_branding_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.CORPORATE_BRANDING_BUTTON))
        click_corporate_branding_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_configuration_dropdown(self):
        click_configuration_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.CONFIGURATION_DROPDOWN))
        click_configuration_dropdown.click()
        time.sleep(3)

    def click_email_configuration_dropdown(self):
        click_email_configuration_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.EMAIL_CONFIGURATION_DROPDOWN))
        click_email_configuration_dropdown.click()
        time.sleep(3)

    def click_subscriptions_dropdown(self):
        click_subscriptions_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.SUBSCRIPTIONS_DROPDOWN))
        click_subscriptions_dropdown.click()
        time.sleep(3)

    def click_localization_dropdown(self):
        click_localization_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.LOCALIZATION_DROPDOWN))
        click_localization_dropdown.click()
        time.sleep(3)

    def click_languages_packages_dropdown(self):
        click_languages_packages_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.LANGUAGE_PACKAGES_DROPDOWN))
        click_languages_packages_dropdown.click()
        time.sleep(3)

    def click_modules_dropdown(self):
        click_modules_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.MODULES_DROPDOWN))
        click_modules_dropdown.click()
        time.sleep(3)

    def click_social_media_authentication_dropdown(self):
        click_social_media_authentication_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.SOCIAL_MEDIA_AUTHENTICATION_DROPDOWN))
        click_social_media_authentication_dropdown.click()
        time.sleep(3)

    def click_register_oauth_client_dropdown(self):
        click_register_oauth_client_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.REGISTER_OAUTH_CLIENT_DROPDOWN))
        click_register_oauth_client_dropdown.click()
        time.sleep(3)

    def click_ldap_configuration_dropdown(self):
        click_ldap_configuration_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocator.LDAP_CONFIGURATION_DROPDOWN))
        click_ldap_configuration_dropdown.click()
        time.sleep(3)
