from selenium.webdriver.common.by import By


class LeaveLocator:
    LEAVE_SIDEBAR = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(3) > a")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    APPLY_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    MY_LEAVE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    EMPLOYMENT_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
    ADD_ENTITLEMENTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')
    EMPLOYEE_ENTITLEMENTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')
    MY_ENTITLEMENTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    REPORTS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
    LEAVE_ENTITLEMENTS_AND_USAGE_REPORT_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')
    MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    CONFIGURE_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
    LEAVE_PERIOD_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[1]')
    LEAVE_TYPES_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[2]')
    WORK_WEEK_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[3]')
    HOLIDAYS_DROPDOWN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[4]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    LEAVE_LIST_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]')

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    ASSIGN_LEAVE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
