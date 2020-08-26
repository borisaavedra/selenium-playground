import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

driver_path = "/mnt/c/Users/bsaavedra/Documents/Personal/selenium-course/chromedriver.exe" #Uso la notación de ruta de UNIX porque uso la terminal de Linux en Win10
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class AutoBrowser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.google.com")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(15)


    def test_browser_navegation(self):
        driver = self.driver

        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("metallica")
        search_field.submit()

        first_link = driver.find_element_by_class_name("rc")
        first_link.find_element_by_tag_name("a").click()
        sleep(4)
        driver.back()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="automatize_browser-report"))