import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class DropDownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://book.theautomatedtester.co.uk/chapter4")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(15)

    def test_drop_down(self):
        exposed_option = ["Selenium IDE", "Selenium Core", "Selenium RC", "Selenium Grid"]   
        active_option = []

        select_options = Select(self.driver.find_element_by_id("selecttype"))
        self.assertEqual(4, len(select_options.options))

        for option in select_options.options:
            active_option.append(option.text)

        self.assertEqual("Selenium IDE", select_options.first_selected_option.text)

        select_options.select_by_visible_text("Selenium RC")
        self.driver.implicitly_wait(10)
        select_options.select_by_visible_text("Selenium Grid")
        self.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="dropdown-report"))