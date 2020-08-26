import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from AmazonPage import AmazonPage

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class AmazonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    def test_load_open_and_find_searchbar(self):
        amazon = AmazonPage(self.driver)
        amazon.open()
        self.assertTrue(amazon.is_loaded)
    
    def test_search(self):
        amazon = AmazonPage(self.driver)
        amazon.search("playstation 4")

    def test_brand(self):
        amazon = AmazonPage(self.driver)
        self.driver.implicitly_wait(10)
        amazon.select_brand("playstation")

    def test_state(self):
        amazon = AmazonPage(self.driver)
        amazon.select_state("nuevo")

    def test_get_products(self):
        amazon = AmazonPage(self.driver)
        amazon.get_products()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="amazon-report"))