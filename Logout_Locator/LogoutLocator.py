from selenium.webdriver.common.by import By


class LogoutLocator:
    USER_DROPDOWN = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-userarea > ul > li > span")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    LOGOUT_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a')