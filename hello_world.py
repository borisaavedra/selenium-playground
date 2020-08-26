import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

driver_path = "/mnt/c/Users/bsaavedra/Documents/Personal/selenium-course/chromedriver.exe" #Uso la notación de ruta de UNIX porque uso la terminal de Linux en Win10
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)

    def test_hello_world(self):
        self.driver.get("https://www.google.com")

    def test_visit_wikipedia(self):
        self.driver.get("https://www.wikipedia.org")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="hello-world-report"))