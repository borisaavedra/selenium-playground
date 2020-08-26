import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.get("http://demo.onestepcheckout.com/")
        cls.driver.maximize_window()

    def test_search_tee(self):
        search_tee = self.driver.find_element_by_name("q")
        search_tee.clear()
        search_tee.send_keys("tee")
        search_tee.submit()

        products = self.driver.find_elements_by_xpath('//*[@id="product-collection-image-398"]')
        self.assertEqual(1, len(products))


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()