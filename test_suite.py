import pytest
from selenium import webdriver

from Admin_Page.AdminPage import AdminPage
from Buzz_Page.BuzzPage import BuzzPage
from Claim_Page.ClaimPage import ClaimPage
from Config.Config import ConfigRestrictedAccess, ConfigLogin
from Dashboard_Page.DashboardPage import DashboardPage
from Directory_Page.DirectoryPage import DirectoryPage
from Leave_Page.LeavePage import LeavePage
from Login_Page.LoginPage import LoginPage
from Logout_Page.LogoutPage import LogoutPage
from Maintenance_Page.MaintenancePage import MaintenancePage
from MyInfo_Page.MyInfoPage import MyInfoPage
from Performance_Page.PerformancePage import PerformancePage
from Pim_Page.PimPage import PimPage
from Recruitment_page.RecruitmentPage import RecruitmentPage
from Time_Page.TimePage import TimePage


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url(ConfigLogin.BaseUrl)
    return login_page


def test_login_page_automation_playground(login):
    login.enter_username(ConfigLogin.USERNAME)
    login.enter_password(ConfigLogin.PASSWORD)
    login.click_login()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_admin_sidebar_on_orange_hrm(login):
    admin_sidebar = AdminPage(login.driver)
    admin_sidebar.click_admin_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_user_management_dropdown()
    admin_sidebar.click_users_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_job_dropdown()
    admin_sidebar.click_job_titles_dropdown()
    admin_sidebar.click_job_dropdown()
    admin_sidebar.click_pay_grades_dropdown()
    admin_sidebar.click_job_dropdown()
    admin_sidebar.click_employment_status_dropdown()
    admin_sidebar.click_job_dropdown()
    admin_sidebar.click_job_categories_dropdown()
    admin_sidebar.click_job_dropdown()
    admin_sidebar.click_work_shifts_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_organization_dropdown()
    admin_sidebar.click_general_information_dropdown()
    admin_sidebar.click_organization_dropdown()
    admin_sidebar.click_locations_dropdown()
    admin_sidebar.click_organization_dropdown()
    admin_sidebar.click_structure_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_qualifications_dropdown()
    admin_sidebar.click_skills_dropdown()
    admin_sidebar.click_qualifications_dropdown()
    admin_sidebar.click_education_dropdown()
    admin_sidebar.click_qualifications_dropdown()
    admin_sidebar.click_licenses_dropdown()
    admin_sidebar.click_qualifications_dropdown()
    admin_sidebar.click_memberships_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_nationalities_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_corporate_branding_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_email_configuration_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_subscriptions_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_localization_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_languages_packages_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_modules_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_social_media_authentication_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_register_oauth_client_dropdown()
    admin_sidebar.click_configuration_dropdown()
    admin_sidebar.click_ldap_configuration_dropdown()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_pim_sidebar_on_orange_hrm(login):
    pim_sidebar = PimPage(login.driver)
    pim_sidebar.click_pim_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    pim_sidebar.click_configuration_dropdown()
    pim_sidebar.click_optional_fields_dropdown()
    pim_sidebar.click_configuration_dropdown()
    pim_sidebar.click_custom_fields_dropdown()
    pim_sidebar.click_configuration_dropdown()
    pim_sidebar.click_data_import_dropdown()
    pim_sidebar.click_configuration_dropdown()
    pim_sidebar.click_reporting_methods_dropdown()
    pim_sidebar.click_configuration_dropdown()
    pim_sidebar.click_termination_reasons_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    pim_sidebar.click_employment_list_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    pim_sidebar.click_add_employee_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    pim_sidebar.click_reports_button()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_leave_sidebar_on_orange_hrm(login):
    leave_sidebar = LeavePage(login.driver)
    leave_sidebar.click_leave_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_apply_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_my_leave_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_employment_dropdown()
    leave_sidebar.click_add_entitlements_dropdown()
    leave_sidebar.click_employment_dropdown()
    leave_sidebar.click_employee_entitlements_dropdown()
    leave_sidebar.click_employment_dropdown()
    leave_sidebar.click_my_entitlements_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_reports_dropdown()
    leave_sidebar.click_leave_entitlements_and_usage_report_dropdown()
    leave_sidebar.click_reports_dropdown()
    leave_sidebar.click_my_leave_entitlements_and_usage_report_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_configure_dropdown()
    leave_sidebar.click_leave_period_dropdown()
    leave_sidebar.click_configure_dropdown()
    leave_sidebar.click_leave_types_dropdown()
    leave_sidebar.click_configure_dropdown()
    leave_sidebar.click_work_week_dropdown()
    leave_sidebar.click_configure_dropdown()
    leave_sidebar.click_holidays_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_leave_list_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    leave_sidebar.click_assign_leave_button()


def test_time_sidebar_on_orange_hrm(login):
    time_sidebar = TimePage(login.driver)
    time_sidebar.click_time_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    time_sidebar.click_time_sheets_dropdown()
    time_sidebar.click_my_time_sheets_dropdown()
    time_sidebar.click_time_sheets_dropdown()
    time_sidebar.click_employee_time_sheets_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    time_sidebar.click_attendance_dropdown()
    time_sidebar.click_my_records_dropdown()
    time_sidebar.click_attendance_dropdown()
    time_sidebar.click_punch_in_out_dropdown()
    time_sidebar.click_attendance_dropdown()
    time_sidebar.click_employee_records_dropdown()
    time_sidebar.click_attendance_dropdown()
    time_sidebar.click_configuration_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    time_sidebar.click_reports_dropdown()
    time_sidebar.click_projects_reports_dropdown()
    time_sidebar.click_reports_dropdown()
    time_sidebar.click_employee_reports_dropdown()
    time_sidebar.click_reports_dropdown()
    time_sidebar.click_advance_summary_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    time_sidebar.click_project_info_dropdown()
    time_sidebar.click_customers_dropdown()
    time_sidebar.click_project_info_dropdown()
    time_sidebar.click_projects_dropdown()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_recruitment_sidebar_on_orange_hrm(login):
    recruitment_sidebar = RecruitmentPage(login.driver)
    recruitment_sidebar.click_recruitment_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    recruitment_sidebar.click_candidates_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    recruitment_sidebar.click_vacancies_button()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_my_info_sidebar_on_orange_hrm(login):
    my_info_sidebar = MyInfoPage(login.driver)
    my_info_sidebar.click_my_info_sidebar()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_performance_sidebar_on_orange_hrm(login):
    performance_sidebar = PerformancePage(login.driver)
    performance_sidebar.click_performance_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    performance_sidebar.click_configure_dropdown()
    performance_sidebar.click_kpis_dropdown()
    performance_sidebar.click_configure_dropdown()
    performance_sidebar.click_trackers_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    performance_sidebar.click_manage_reviews_1_button()
    performance_sidebar.click_manage_reviews_2_button()
    performance_sidebar.click_manage_reviews_1_button()
    performance_sidebar.click_my_reviews_dropdown()
    performance_sidebar.click_manage_reviews_1_button()
    performance_sidebar.click_employee_reviews_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    performance_sidebar.click_my_trackers_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    performance_sidebar.click_employee_trackers_button()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_dashboard_sidebar_on_orange_hrm(login):
    dashboard_sidebar = DashboardPage(login.driver)
    dashboard_sidebar.click_dashboard_sidebar()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_maintenance_sidebar_on_orange_hrm(login):
    maintenance_sidebar = MaintenancePage(login.driver)
    maintenance_sidebar.click_maintenance_sidebar()

    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    # RESTRICTED ACCESS --------------------------------------------------------------------------------------------------
    maintenance_sidebar.enter_password(ConfigRestrictedAccess.PASSWORD)
    maintenance_sidebar.click_confirm_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    maintenance_sidebar.click_purge_records_dropdown()
    maintenance_sidebar.click_employee_records_dropdown()
    maintenance_sidebar.click_purge_records_dropdown()
    maintenance_sidebar.click_candidate_records_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    maintenance_sidebar.click_access_records_button()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_directory_sidebar_on_orange_hrm(login):
    directory_sidebar = DirectoryPage(login.driver)
    directory_sidebar.click_directory_sidebar()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_claim_sidebar_on_orange_hrm(login):
    claim_sidebar = ClaimPage(login.driver)
    claim_sidebar.click_claim_sidebar()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    claim_sidebar.click_configuration_dropdown()
    claim_sidebar.events_dropdown()
    claim_sidebar.click_configuration_dropdown()
    claim_sidebar.click_expense_types_dropdown()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    claim_sidebar.click_submit_claim_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    claim_sidebar.my_claims_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    claim_sidebar.click_employee_claims_button()
    # --------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------
    claim_sidebar.click_assign_claim_button()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_buzz_sidebar_on_orange_hrm(login):
    buzz_sidebar = BuzzPage(login.driver)
    buzz_sidebar.click_buzz_sidebar()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

def test_logout_sidebar_on_orange_hrm(login):
    logout_sidebar = LogoutPage(login.driver)
    logout_sidebar.click_user_dropdown()
    logout_sidebar.click_logout_button()
