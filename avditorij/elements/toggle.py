from enum import Enum

from selenium.webdriver.common.by import By

from base.base_page_element import BasePageElement


class ToggleSwitch(BasePageElement):
    def __init__(self, element):
        super().__init__(element)


class ToggleButton(BasePageElement):
    def __init__(self, element):
        super().__init__(element)
        '''
        OPTION_A = 'option A button text'
        '''
    def select_option(self, option):
        self.find_element(By.XPATH, self.make_xpath(option)).click()
        self.log.info(f'Selecting option: {option}')

    def make_xpath(self, option):
        return f'.//a[contains(text(), "{option}")]'

