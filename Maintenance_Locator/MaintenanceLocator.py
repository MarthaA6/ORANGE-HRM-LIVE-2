from selenium.webdriver.common.by import By


class MaintenanceLocator:
    MAINTENANCE_SIDEBAR = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(10) > a")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# ADMINISTRATOR_ACCESS

    PASSWORD = (By.CSS_SELECTOR, "#app > div.orangehrm-admin-access-container > div.orangehrm-card-container > form > div:nth-child(6) > div > div:nth-child(2) > input")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "#app > div.orangehrm-admin-access-container > div.orangehrm-card-container > form > div.orangehrm-admin-access-button-container > button.oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-admin-access-button")


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    PURGE_RECORDS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
    EMPLOYEE_RECORDS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]')
    CANDIDATE_RECORDS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    ACCESS_RECORDS_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')





