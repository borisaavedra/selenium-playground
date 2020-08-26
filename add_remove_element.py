import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class AddRemoveElement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://the-internet.herokuapp.com/")


    def test_add_remove_element(self):
        driver = self.driver.find_element_by_link_text("Add/Remove Elements").click()

        added_elements = int(input("How many elements you wan to add? "))
        deleted_elements = int(input("How many elements wan to delete? "))

        for i in range(added_elements):
            self.driver.find_element_by_xpath('//*[@id="content"]/div/button').click()

        sleep(4)

        for i in range(deleted_elements):
            try:
                self.driver.find_element_by_class_name("added-manually").click()
            except:
                break
        
        total_elements = deleted_elements - added_elements
        if total_elements > 0:
            print("You trying to delete more elements that you create, caimán!")
        else:
            print(f"There is {-1*total_elements} on the screen")

        sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="find_element-report"))