from selenium.webdriver.common.by import By
from basepage import BasePage

class Main(BasePage):
    #Declares a variables for objects
    STR_URL = 'https://shop.circles.life/my_profile'
    TITLE = 'Unlimit your telco. Now'
    FNAME_TEXT = (By.XPATH, '//div[./label[text()="First Name"]]//input')
    LNAME_TEXT = (By.XPATH, '//div[./label[text()="Last Name"]]//input')
    EMAIL_TEXT = (By.XPATH, '//div[./label[text()="Email"]]//input')

    def check_url(self):
        """Verify URL"""
        currenturl = self.driver.current_url
        assert self.STR_URL == currenturl, 'URL not expected. Actual: ' + currenturl + ', Expected: ' + self.STR_URL 
        #return false#self.STR_URL == self.driver.current_url

    def check_title(self):
        """Verify Title of the Page"""
        currenttitle = self.driver.title
        assert self.TITLE in currenttitle, 'Title not expected. Actual: ' + currenttitle + ', Expected: ' + self.TITLE

    def verify_firstname(self, fname):
        element = self.driver.find_element(*self.FNAME_TEXT)
        actual = element.get_attribute('value')
        is_verified = fname == actual
        assert is_verified, 'First Name not expected. Actual : ' + actual + ', Expected: ' + fname

    def verify_lastname(self, lname):
        element = self.driver.find_element(*self.LNAME_TEXT)
        actual = element.get_attribute('value')
        is_verified = lname == actual
        assert is_verified, 'Last Name not expected. Actual : ' + actual + ', Expected: ' + lname

    def verify_email(self, email):
        element = self.driver.find_element(*self.EMAIL_TEXT)
        actual = element.get_attribute('value')
        is_verified = email == actual
        assert is_verified, 'Email not expected. Actual : ' + actual + ', Expected: ' + email