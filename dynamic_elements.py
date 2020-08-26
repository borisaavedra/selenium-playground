import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class DynamicElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://the-internet.herokuapp.com/")


    def test_dynamic_elements(self):
        driver = self.driver

        driver.find_element_by_link_text("Disappearing Elements").click()

        tries = 0

        while True:
            tries += 1
            nav = driver.find_element_by_tag_name("ul")
            menu_items = nav.find_elements_by_tag_name("li")
            try:
                self.assertEqual(5, len(menu_items))
                break
            except:
                driver.refresh()
        
        print(f"Found The Gallery item in {tries} times")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="find_element-report"))