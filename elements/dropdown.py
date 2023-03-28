import time

from overrides import overrides
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from base.base_page_element import BasePageElement


class Dropdown(BasePageElement):
    def __init__(self, element):
        super().__init__(element)
        self.expand_button_xpath = ...
        self.option_xpath = './/a[contains(@title, {title})]'

    def expand(self):
        if not self.is_expanded:
            # self.find_element(By.XPATH, self.expand_button_xpath).click()
            # self.init_expanded()
            # self.wait_for_visibility(5)
            # WebDriverWait.until(EC.element_to_be_clickable(self.about_xpath))
            self.click()
            time.sleep(2)
            self.init_expanded()

    def collapse(self):
        if self.is_expanded:
            # print(f'COLLAPSE DROPDOWN XPATH JE {self.expand_button_xpath}')
            # self.find_element(By.XPATH, self.expand_button_xpath).click()
            # self.init_collapsed()
            self.click()
            time.sleep(2)
            self.init_collapsed()

    @property
    def is_expanded(self):
        print(f'is displayed: {self.is_displayed()}')
        return self.is_displayed()

    def init_expanded(self):
        pass

    def init_collapsed(self):
        pass

    def select_by_text(self, text):
        assert self.is_expanded, 'Dropdown is not expanded'
        self.find_element(By.XPATH, self.option_xpath.format(text)).click()


class HeaderDropdown(Dropdown):
    def __init__(self, element):
        super().__init__(element)

    def __enter__(self):
        self.expand()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.collapse()
        except StaleElementReferenceException:
            print('Dropdown has already closed automatically')
        return self

    @property
    @overrides
    def is_expanded(self):
        return 'menu-level1-open' in self.get_attribute_or_property('class')