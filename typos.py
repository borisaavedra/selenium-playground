import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class Typos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://the-internet.herokuapp.com/typos")


    def test_typos(self):
        driver = self.driver
        
        correct_text = "Sometimes you'll see a typo, other times you won't."
        tries = 1

        while True:
            text = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            try:
                self.assertEqual(text.text, correct_text)
                break
            except:
                tries += 1
                driver.refresh()

        print(f"Found the right text in {tries} tries")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="find_element-report"))