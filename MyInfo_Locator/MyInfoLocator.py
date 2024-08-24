from selenium.webdriver.common.by import By


class MyInfoLocator:
    MY_INFO_SIDEBAR = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a")
