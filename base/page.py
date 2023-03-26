from selenium.webdriver.common.by import By

from elements.header import Header


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    # @property
    # def current_page(self):
    #     return self.driver.find_element(By.XPATH, '/html/body')

    def get_header(self):
        return Header(self.driver.find_element(By.XPATH, '//ul[contains(@id, "main-menu")]'))