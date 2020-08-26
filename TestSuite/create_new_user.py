import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class CreateNewUserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.get("http://demo.onestepcheckout.com/")
        cls.driver.maximize_window()

    def test_new_user(self):
        driver = self.driver

        account_btn = driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a')
        self.assertTrue(self.is_displayed_enabled(account_btn))
        account_btn.click()

        login_btn = driver.find_element_by_link_text("Log In")
        self.assertTrue(self.is_displayed_enabled(login_btn))
        login_btn.click()

        create_account_btn = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(self.is_displayed_enabled(create_account_btn))
        create_account_btn.click()

        first_name = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[1]/ul/li[1]/div/div[1]/div/input')
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        password = driver.find_element_by_id("password")
        confirmation = driver.find_element_by_id("confirmation")
        newsletter_subscription = driver.find_element_by_id("is_subscribed")
        submit_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(self.is_displayed_enabled(first_name) and
                        self.is_displayed_enabled(last_name) and
                        self.is_displayed_enabled(email_address) and
                        self.is_displayed_enabled(password) and
                        self.is_displayed_enabled(confirmation) and
                        self.is_displayed_enabled(newsletter_subscription) and
                        self.is_displayed_enabled(submit_btn))
        
        first_name.send_keys("Test Name")
        last_name.send_keys("Test Last Name")
        email_address.send_keys("test_venezuela_2@test.com")
        password.send_keys("password")
        confirmation.send_keys("password")
        newsletter_subscription.click()
        submit_btn.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_displayed_enabled(self, driver):
        return driver.is_displayed() and driver.is_enabled()
