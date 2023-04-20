from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from pages.header import Header


class Page(BasePageElement):
    def __init__(self, element):
        super().__init__(element)

    # @property
    # def current_page(self):
    #     return self.driver.find_element(By.XPATH, '/html/body')

    def get_header(self):
        return Header(self.driver.find_element(By.XPATH, '//ul[contains(@id, "main-menu")]'))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self