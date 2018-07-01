from selenium.webdriver.common.by import By
from basepage import BasePage
import ex_fbpage

class Main(BasePage):
    #Declares a variables for objects
    STR_URL = 'https://shop.circles.life/login'
    TITLE = 'Unlimit your telco. Now'
    EMAIL_TEXT = (By.NAME, 'email')
    PASSWORD_TEXT = (By.NAME, 'password')
    SIGNIN_BUTTON = (By.XPATH, '//button[text()="Sign In"]')
    FB_BUTTON = (By.CSS_SELECTOR, 'button.facebook-login-button')

    def check_url(self):
        """Verify URL"""
        currenturl = self.driver.current_url
        assert self.STR_URL in currenturl, 'URL not expected. Actual: ' + currenturl + ', Expected: ' + self.STR_URL 
        #return false#self.STR_URL == self.driver.current_url

    def check_title(self):
        """Verify Title of the Page"""
        currenttitle = self.driver.title
        assert self.TITLE in currenttitle, 'Title not expected. Actual: ' + currenttitle + ', Expected: ' + self.TITLE 

    def input_email_address(self, email):
        element = self.driver.find_element(*self.EMAIL_TEXT)
        element.send_keys(email)

    def input_password(self, passwd):
        element = self.driver.find_element(*self.PASSWORD_TEXT)
        element.send_keys(passwd)

    def click_signin_button(self):
        element = self.driver.find_element(*self.SIGNIN_BUTTON)
        element.click()

    def do_login(self, email, passwd):
        self.input_email_address(email)
        self.input_password(passwd)
        self.click_signin_button()

    def do_login_facebook(self, email, passwd):
        fbBtn = self.driver.find_element(*self.FB_BUTTON)
        fbBtn.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        fb = ex_fbpage.Main(self.driver)

        #Do Login FB
        fb.do_login(email, passwd)

        self.driver.switch_to.window(self.driver.window_handles[0])
