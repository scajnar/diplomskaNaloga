import inspect

from overrides import overrides
from selenium.webdriver.common import log
from selenium.webdriver.common.by import By

from base.base_page_element import BasePageElement
from elements.button import Button
from elements.dropdown import HeaderDropdown
from pages.header_elements.izobrazevanje import IzobrazevanjeDropdown
from pages.header_elements.o_fakulteti import OFakultetiDropdown


class Header(BasePageElement):


    class ResearchDropdown(HeaderDropdown):
        def __init__(self, element):
            super().__init__(element)

    class NewsDropdown(HeaderDropdown):
        def __init__(self, element):
            super().__init__(element)

    class Covid19InfoDropdown(HeaderDropdown):
        def __init__(self, element):
            super().__init__(element)

    def __init__(self, element):
        super().__init__(element)
        self.o_fakulteti_text = 'O fakulteti'
        self.izobrazevanje_text = 'Izobraževanje'
        self.raziskovanje_text = 'Raziskovanje'
        self.aktualno_text = 'Aktualno'
        # self.covid_19_info_text = 'COVID-19 info'

        self.o_fakulteti_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.o_fakulteti_text}")]/ancestor::li'
        self.izobrazevanje_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.izobrazevanje_text}")]/ancestor::li'
        self.raziskovanje_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.raziskovanje_text}")]/ancestor::li'
        self.aktualno_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.aktualno_text}")]/ancestor::li'
        # self.covid_19_info_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.covid_19_info_text}")]/ancestor::li'

        self.o_fakulteti_dropdown = OFakultetiDropdown(self.find_element(By.XPATH, self.o_fakulteti_xpath))
        self.izobrazevanje_dropdown = IzobrazevanjeDropdown(self.find_element(By.XPATH, self.izobrazevanje_xpath))
        self.raziskovanje_dropdown = Button(self.find_element(By.XPATH, self.raziskovanje_xpath))
        self.aktualno_dropdown = Button(self.find_element(By.XPATH, self.aktualno_xpath))
        # self.covid_19_info_button = Button(self.find_element(By.XPATH, self.covid_19_info_xpath))


