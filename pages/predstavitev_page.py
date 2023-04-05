from selenium.webdriver.common.by import By

from base.page import Page
from elements.toggle import ToggleButton


class PredstavitevPage(Page):

    class PredstavitevToggle(ToggleButton):
        def __init__(self, element):
            super().__init__(element)
            self.PREDSTAVITEV = 'Predstavitev'
            self.POSLANSTVO_IN_VIZIJA = 'Poslanstvo in vizija'
            self.ZGODOVINA = 'Zgodovina'
            self.KATEDRE_IN_LABORATORIJI = 'Katedre in laboratoriji'
            self.ORGANIZIRANOST_FAKULTETE = 'Organiziranost fakultete'
            self.KATALOG_IJZ = 'Katalog IJZ'
            self.KJE_SMO = 'Kje smo'
            self.MEDIJSKO_SREDISCE = 'Medijsko središče'
            self.CENIK_NAJEMA_PROSTOROV = 'Cenik najema prostorov'
            self.NACRT_PROSTOROV = 'Nacrt prostorov'
            self.DOKUMENTI = 'Dokumenti'
            self.VARSTVO_OSEBNIH_PODATKOV = 'Varstvo osebnih podatkov'
            self.ZAUPNA_OSEBA = 'Zaupna oseba'

    def __init__(self, element):
        super().__init__(element)
        self.toggle_predstavitev_xpath = './/div[contains(@class, "btn-group")]'
        self.toggle_predstavitev = self.PredstavitevToggle(self.find_element(By.XPATH, self.toggle_predstavitev_xpath))

