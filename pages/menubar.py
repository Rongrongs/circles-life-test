import time
from selenium.webdriver.common.by import By
from basepage import BasePage

class Main(BasePage):
    #Declares a variables for objects
    MENU_BUTTON = (By.CSS_SELECTOR, 'div.hidden-lg-up button')
    MYACCOUNT_LINK = (By.XPATH, '//a[@href="/my_profile"]')
    LOGOUT_LINK = (By.XPATH, '//a[contains(text(), "Log Out")]')

    def open_menubar(self):
        element = self.driver.find_element(*self.MENU_BUTTON)
        element.click()

    def click_myaccount(self):
        self.open_menubar()
        time.sleep(1)
        element = self.driver.find_element(*self.MYACCOUNT_LINK)
        element.click()

    def click_logout(self):
        self.open_menubar()
        time.sleep(1)
        element = self.driver.find_element(*self.LOGOUT_LINK)
        element.click()