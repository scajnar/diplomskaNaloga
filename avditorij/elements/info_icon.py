from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement


class InfoIcon(BasePageElement):
    def __init__(self, element):
        super().__init__(element)
        self.popup_xpath = '/following-sibling::div[contains(@class, "popover")]'

    def is_popup_displayed(self):
        return self.find_elements(By.XPATH, self.popup_xpath) != []

    def get_popup(self):
        assert self.is_popup_displayed(), 'Popup is not opened'  # Popup needs to be opened explicitly
        return self.find_element(By.XPATH, self.popup_xpath)

    def open_popup(self):  # Used instead of clicking to avoid ambiguity
        assert not self.is_popup_displayed(), 'Popup is already open'
        self.click()

    def close_popup(self):
        assert self.is_popup_displayed(), 'Popup is already closed'
        self.click()