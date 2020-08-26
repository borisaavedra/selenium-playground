import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

driver_path = "/mnt/c/Users/bsaavedra/Documents/Personal/selenium-course/chromedriver.exe" #Uso la notación de ruta de UNIX porque uso la terminal de Linux en Win10
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://demo.onestepcheckout.com/")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(15)


    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")


    def test_subscribe_field(self):
        subscribe_field = self.driver.find_element_by_name("email")


    def test_block_text(self):
        block = self.driver.find_element_by_class_name("block-title")

    def test_nav_bar(self):
        nav = self.driver.find_element_by_class_name("nav-primary")
        links = nav.find_elements_by_tag_name("li")
        self.assertEqual(32, len(links))

    def test_youtube_icon(self):
        youtube_icon = self.driver.find_element_by_css_selector("a em.youtube")
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="find_element-report"))