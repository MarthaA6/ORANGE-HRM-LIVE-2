import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Recruitment_Locator.RecruitmentLocator import RecruitmentLocator


class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver

    def click_recruitment_sidebar(self):
        click_recruitment_sidebar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RecruitmentLocator.RECRUITMENT_SIDEBAR))
        click_recruitment_sidebar.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_candidates_button(self):
        click_candidates_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RecruitmentLocator.CANDIDATES_BUTTON))
        click_candidates_button.click()
        time.sleep(3)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

    def click_vacancies_button(self):
        click_vacancies_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RecruitmentLocator.VACANCIES_BUTTON))
        click_vacancies_button.click()
        time.sleep(3)