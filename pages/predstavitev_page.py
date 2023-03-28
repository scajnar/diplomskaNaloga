from selenium.webdriver.common.by import By

from base.page import Page
from elements.toggle import ToggleButton


class PredstavitevPage(Page):

    class PredstavitevToggle(ToggleButton):
        def __init__(self, element):
            super().__init__(element)
            self.PREDSTAVITEV = 'Predstavitev'
            self.POSLANSTVO_IN_VIZIJA = 'Poslanstvo in vizija'

    def __init__(self, element):
        super().__init__(element)
        predstavitev_text = 'Predstavitev'
        poslanstvo_in_vizija_text = 'Poslanstvo in vizija'
        self.toggle_predstavitev_xpath = './/div[contains(@class, "btn-group")]'
        self.toggle_predstavitev = self.PredstavitevToggle(self.find_element(By.XPATH, self.toggle_predstavitev_xpath))

