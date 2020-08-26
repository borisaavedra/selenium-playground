import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AmazonPage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = "https://www.amazon.com/"

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.NAME, "field-keywords")))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name("field-keywords")
        return input_field.get_attribute("value")

    def open(self):
        self._driver.get(self._url)

    def click_submit(self):
        input_field = self._driver.find_element_by_name("field-keywords")
        input_field.submit()

    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name("field-keywords")
        input_field.send_keys(keyword)

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()
    
    def select_brand(self, keyword):
        brands = self._driver.find_elements(By.CLASS_NAME, "a-size-base")
        for b in brands:
            if b.text.lower() == keyword:
                b.click()
                break

    def select_state(self, keyword):
        states = WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-size-base.a-color-base")))
        for state in states:
            if state.text.lower() == keyword:
                state.click()
                break
    
    def get_products(self):
        wait = WebDriverWait(self._driver, 20)
        products_name = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")))
        for i in products_name:
            print(f"----- {i.text}")