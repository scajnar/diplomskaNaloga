from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.base_elements.page import Page
from avditorij.elements.button import Button
from avditorij.elements.dropdown import Dropdown
from avditorij.elements.input import Input


class NadzornaPloscaPage(Page):
    def __init__(self, element):
        super().__init__(element)
        self.casovnica_text = "Časovnica"
        self.koledar_text = "Koledar"
        self.casovnica_xpath = f'.//h5[text()="{self.casovnica_text}"]/parent::div[contains(@class, "card-body")]'
        self.koledar_xpath = f'.//h5[text()="{self.koledar_text}"]/parent::div[contains(@class, "card-body")]'

        self.casovnica = self.find_element(By.XPATH, self.casovnica_xpath)
        self.koledar = self.find_element(By.XPATH, self.koledar_xpath)


    class Casovnica(BasePageElement):
        def __init__(self, element):
            super().__init__(element)
            self.title_xpath = './/h5'
            self.naslednjih_x_dni_dropdown_xpath = \
                './/span[contains(@id, "timeline-day")]/ancestor::div[contains(@class, "dropdown")]'
            self.razvrsti_po_dropdown_xpath = \
                './/span[contains(@id, "timeline-view")]/ancestor::div[contains(@data-region, "view-selector")]'
            self.search_input_xpath = './/input[@id="searchinput"]'

            self.naslednjih_x_dni_dropdown = Dropdown(self.find_element(By.XPATH, self.naslednjih_x_dni_dropdown_xpath))
            self.razvrsti_po_dropdown = Dropdown(self.find_element(By.XPATH, self.razvrsti_po_dropdown_xpath))
            self.search_input = Input(self.find_element(By.XPATH, self.search_input_xpath))


    class Koledar(BasePageElement):
        def __init__(self, element):
            super().__init__(element)
            self.full_calendar_button_text = 'Full calendar'
            self.upravljanje_narocnin_button_text = 'Upravljanje naročnin'

            self.title_xpath = './/h5'
            self.predmeti_dropdown_xpath = './/select[contains(@id, "calendar-course")]'
            self.nov_dogodek_button_xpath = './/button[@data-action="new-event-button"]'
            self.current_date_text_xpath = './/h4[@class="current"]'
            self.previous_month_button_xpath = './/a[@class="arrow_link previous"]'
            self.next_month_button_xpath = './/a[@class="arrow_link next"]'
            self.calendar_days_xpath = './/td[@data-region="day"]'

            self.predmeti_dropdown = Dropdown(self.find_element(By.XPATH, self.predmeti_dropdown_xpath))
            self.nov_dogodek_button = Button(self.find_element(By.XPATH, self.nov_dogodek_button_xpath))
            self.previous_month_button = Button(self.find_element(By.XPATH, self.previous_month_button_xpath))
            self.next_month_button = Button(self.find_element(By.XPATH, self.next_month_button_xpath))
            self.full_calendar_button = Button(self.find_element(By.XPATH, self.full_calendar_button_text))
            self.upravljanje_narocnin_button = \
                Button(self.find_element(By.XPATH, self.upravljanje_narocnin_button_text))
            self.calendar_days = [self.CalendarDay(x) for x in self.find_elements(By.XPATH, self.calendar_days_xpath)]

        class CalendarDay(BasePageElement):
            def __init__(self, element):
                super().__init__(element)