import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

driver_path = "/mnt/c/Users/bsaavedra/Documents/Personal/selenium-course/chromedriver.exe" #Uso la notación de ruta de UNIX porque uso la terminal de Linux en Win10
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class LogInTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.get("http://demo.onestepcheckout.com/")
        cls.driver.maximize_window()

    def test_log_in(self):
        driver = self.driver

        account_btn = driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a')
        self.assertTrue(self.is_displayed_enabled(account_btn))
        account_btn.click()

        login_btn = driver.find_element_by_link_text("Log In")
        self.assertTrue(self.is_displayed_enabled(login_btn))
        login_btn.click()

        email_input = driver.find_element_by_id('email')

        password_input = driver.find_element_by_id("pass")

        login_submit_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div[2]/button/span/span')

        self.assertTrue(self.is_displayed_enabled(email_input) and
                        self.is_displayed_enabled(password_input) and
                        self.is_displayed_enabled(login_submit_btn))
        
        email_input.send_keys("test_venezuela_2@test.com")
        password_input.send_keys("password")
        login_submit_btn.click()

    def test_my_account_page(self):
        driver = self.driver
        self.assertEqual("My Account", driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_displayed_enabled(self, driver):
        return driver.is_displayed() and driver.is_enabled()
