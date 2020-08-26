import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class AssertionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.get("http://demo.onestepcheckout.com/")
        cls.driver.implicitly_wait(60)
        cls.driver.maximize_window()


    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    
    def test_pinterest_icon(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "pinterest"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
            return True

        except NoSuchElementException as variable:
            return False