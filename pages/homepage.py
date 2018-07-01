from selenium.webdriver.common.by import By
from basepage import BasePage

class Main(BasePage):
    #Declares a variables for objects
    STR_URL = 'https://pages.circles.life/'
    TITLE = 'Circles.Life | Unlimit your telco. Now'
    BUY_BUTTON = (By.XPATH, '(//nav[@id="site-navigation"]//a[contains(@href, "login")])[2]') #MOBILE

    def check_url(self):
        """Verify URL"""
        currenturl = self.driver.current_url
        assert self.STR_URL == currenturl, 'URL not expected. Actual: ' + currenturl + ', Expected: ' + self.STR_URL 
        #return false#self.STR_URL == self.driver.current_url

    def check_title(self):
        """Verify Title of the Page"""
        currenttitle = self.driver.title
        assert self.TITLE in currenttitle, 'Title not expected. Actual: ' + currenttitle + ', Expected: ' + self.TITLE 

    def click_buynow_button(self):
        element = self.driver.find_element(*self.BUY_BUTTON)
        element.click()