from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement


class Input(BasePageElement):
    def __init__(self, element):
        super().__init__(element)
