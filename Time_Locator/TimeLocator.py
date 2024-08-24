from selenium.webdriver.common.by import By


class TimeLocator:
    TIME_SIDEBAR = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(4) > a")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    TIME_SHEETS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
    MY_TIME_SHEETS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]')
    EMPLOYEE_TIME_SHEETS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    ATTENDANCE_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
    MY_RECORDS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]')
    PUNCH_IN_OUT_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')
    EMPLOYEE_RECORDS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]')
    CONFIGURATION_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    REPORTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
    PROJECT_REPORTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')
    EMPLOYEE_REPORTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')
    ADVANCE_SUMMARY_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    PROJECT_INFO_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
    CUSTOMERS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')
    PROJECTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')

