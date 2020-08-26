import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

driver_path = "/mnt/c/Users/bsaavedra/Documents/Personal/selenium-course/chromedriver.exe" #Uso la notación de ruta de UNIX porque uso la terminal de Linux en Win10
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

class Tables(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://the-internet.herokuapp.com/tables")


    def test_tables(self):
        driver = self.driver

        person = {}
        big_list = []
        keys = []
        i = 1; j = 1; x = 1
        y = 0; r = 0
        
        while True:
            try:
                header = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i}]/span')
                keys.append(header.text)
                i += 1
            except:
                break


        while True:
            try:
                driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{x}]/td[1]')
                while True:
                    try:
                        item = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{x}]/td[{j}]')
                        person[keys[y]] = item.text
                        j += 1; y += 1 
                    except:
                        break
                big_list.append(person.copy())
                print(big_list)
                j = 1; x += 1; y = 0; r += 1
            except:
                break

        for g in big_list:
            print(g)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="find_element-report"))