import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class AlertTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://demo.onestepcheckout.com/")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(15)

    def test_remove_alert(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys("tee")
        submit_btn = driver.find_element_by_xpath('//*[@id="search_mini_form"]/div[1]/button')
        submit_btn.click()

        compare_link = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[4]/div/div[3]/ul/li[2]/a')
        compare_link.click()

        clear_btn = driver.find_element_by_link_text("Clear All")
        clear_btn.click()

        alert = driver.switch_to_alert()
        alert_text = alert.text
        self.assertTrue("Are you sure you would like to remove all products from your comparison?", alert_text)
        alert.accept()

        product_list_icon = driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/p/a').click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="remove-alert-report"))