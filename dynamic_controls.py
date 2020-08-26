import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class DynamicControl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://the-internet.herokuapp.com/dynamic_controls")


    def test_dynamic(self):
        driver = self.driver

        driver.find_element_by_css_selector('#checkbox > input[type=checkbox]').click()

        wait = WebDriverWait(driver, 10)
        
        btn_remove = driver.find_element_by_css_selector('#checkbox-example > button')
        btn_remove.click()
        
        message = wait.until(EC.element_to_be_clickable((By.ID, 'message')))

        btn_add = driver.find_element_by_css_selector("#checkbox-example > button")
        btn_add.click()

        message = wait.until(EC.element_to_be_clickable((By.ID, "message")))
        self.assertEqual(message.text, "It's back!")

        enable_btn = driver.find_element_by_css_selector("#input-example > button")
        enable_btn.click()

        text_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input[type=text]")))

        text_field.send_keys("Hola, bebé!")

        sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="find_element-report"))