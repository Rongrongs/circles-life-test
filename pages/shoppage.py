from selenium.webdriver.common.by import By
from basepage import BasePage

class Main(BasePage):
    #Declares a variables for objects
    STR_URL = 'https://shop.circles.life/plan'
    TITLE = 'Unlimit your telco. Now'

    def check_url(self):
        """Verify URL"""
        currenturl = self.driver.current_url
        assert self.STR_URL == currenturl, 'URL not expected. Actual: ' + currenturl + ', Expected: ' + self.STR_URL 
        #return false#self.STR_URL == self.driver.current_url

    def check_title(self):
        """Verify Title of the Page"""
        currenttitle = self.driver.title
        assert self.TITLE in currenttitle, 'Title not expected. Actual: ' + currenttitle + ', Expected: ' + self.TITLE 