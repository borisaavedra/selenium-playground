import unittest, csv
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from ddt import ddt, data, unpack

# You have to add the complete path to the browser 
# driver (in my case: Chrome) ann the path to the 
# Brave Browser (which I love 😎)

option = webdriver.ChromeOptions()
option.binary_location = brave_path

def get_data(file_name):
    rows = []
    file_data = open(file_name, "r")
    reader = csv.reader(file_data)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return list(rows)

@ddt
class DdtSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://demo.onestepcheckout.com/")

    @data(*get_data("testdata.csv"))
    @unpack
    def test_ddt(self, search_value, expected_value):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_class_name("product-name")

        expected_value = int(expected_value)

        if expected_value > 0:
            self.assertEqual(expected_value, len(products))
        else:
            message = driver.find_element_by_class_name("note-msg")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="ddt-report"))