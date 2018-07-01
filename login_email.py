import time
import unittest
from selenium import webdriver
from pages import homepage, loginpage, shoppage, menubar, accountpage

class LoginEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.set_window_size(1920, 1080)
        self.driver.get("https://www.circles.life")

    def test_login_with_email(self):
        """
        Steps :
        1. Open Homepage of Circles.Life
        2. Click Buy Now Button
        3. Check Redirect to Login Page
        4. Login using e-mail address
        5. Check if Login success by checking the UI
        6. Go to My Account
        7. Check e-mail correct
        8. Logout
        """

        #Load the main page
        home = homepage.Main(self.driver)
        #Checks if page redirects to pages.circles.life
        home.check_url()

        #Click buynow button and check redirect
        home.click_buynow_button()
        
        #Wait page to be loaded
        time.sleep(5)

        login = loginpage.Main(self.driver)
        login.check_url()

        #Do login with valid user
        login.do_login('your.email@gmail.com', 'yourpassword')

        #Wait login processed
        time.sleep(5)

        #Verify Shop homepage
        shop = shoppage.Main(self.driver)
        shop.check_url()

        menu = menubar.Main(self.driver)
        menu.click_myaccount()

        time.sleep(5)
        #Verify My Account
        acc = accountpage.Main(self.driver)
        acc.check_url()

        acc.verify_firstname('FirstName')
        acc.verify_lastname('LastName')
        acc.verify_email('your.email@gmail.com')

        #Logout
        menu = menubar.Main(self.driver)
        menu.click_logout()

        time.sleep(5)
        login.check_url()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()