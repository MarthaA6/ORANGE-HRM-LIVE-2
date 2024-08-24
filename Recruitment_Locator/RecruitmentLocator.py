from selenium.webdriver.common.by import By


class RecruitmentLocator:
    RECRUITMENT_SIDEBAR = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    CANDIDATES_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    VACANCIES_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
