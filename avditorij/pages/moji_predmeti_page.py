from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.base_elements.page import Page
from avditorij.elements.dropdown import Dropdown
from avditorij.elements.info_icon import InfoIcon
from avditorij.elements.input import Input


class MojiPredmetiPage(Page):
    def __init__(self, element):
        super().__init__(element)
        self.title_xpath = './/h1'
        self.subject_cards_xpath = './/div[@class="card dashboard-card"]'
        self.filter_dropdown_xpath = './/button[@aria-label="Spustni meni s skupki"]/parent::div'
        self.search_input_xpath = './/input[@id="searchinput"]'
        self.sorting_order_dropdown_xpath = './/button[@aria-label="Razvrščanje spustnega menija"]/parent::div'
        self.view_type_dropdown_xpath = './/button[@aria-label="Prikaži spustni meni"]/parent::div'

        self.filter_dropdown = Dropdown(self.find_element(By.XPATH, self.filter_dropdown_xpath))
        self.search_input = Input(self.find_element(By.XPATH, self.search_input_xpath))
        self.sorting_order_dropdown = Dropdown(self.find_element(By.XPATH, self.sorting_order_dropdown_xpath))
        self.view_type_dropdown = Dropdown(self.find_element(By.XPATH, self.view_type_dropdown_xpath))
        self.subject_cards = [self.SubjectCard(x) for x in self.find_elements(By.XPATH, self.subject_cards_xpath)]


    class SubjectCard(BasePageElement):
        def __init__(self, element):
            super().__init__(element)
            self.category_name_text_xpath = './/span[contains(@class, "categoryname")]'
            self.three_dot_options_button_xpath = './/button[@data-toggle="dropdown"]'
            self.subject_name_xpath = './/span[contains(@class, "multiline")]'
            self.badge_name_xpath = './/span[contains(@class, "badge")]'
            self.three_dot_options_button = \
                self.ThreeDotsOptionsButton(self.find_element(By.XPATH, self.three_dot_options_button_xpath))


        class ThreeDotsOptionsButton(InfoIcon):
            def __init__(self, element):
                super().__init__(element)

