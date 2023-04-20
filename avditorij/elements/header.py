from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.elements.button import Button


class Header(BasePageElement):
    xpath = '//nav[contains(@class, "navbar")]'
    def __init__(self, element):
        super().__init__(element)
        self.domov_button_text = 'Domov'
        self.nadzorna_plosca_button_text = 'Nadzorna plošča'
        self.moji_predmeti_button_text = 'Moji predmeti'

        self.fri_logo_button_xpath = './/a[contains(@class, "navbar-brand")]'
        self.domov_button_xpath = f'.//a[contains(@role, "menuitem") and contains(text(), "{self.domov_button_text}")]'
        self.nadzorna_plosca_button_xpath = f'.//a[contains(@role, "menuitem") and contains(text(), "{self.nadzorna_plosca_button_text}")]'
        self.moji_predmeti_button_xpath = f'.//a[contains(@role, "menuitem") and contains(text(), "{self.moji_predmeti_button_text}")]'
        self.notification_dropdown_xpath = f'//i[contains(@title, "Preklopi meni")]'
        self.messages_dropdown_xpath = './/i[contains(@title, "Preklopi predal")]'
        self.user_dropdown_xpath = './/a[contains(@id, "user-menu-toggle")]'
        self.edit_mode_toggle_button_xpath = './/span[@class="custom-control-label"]/parent::div'

        self.domov_button = Button(self.find_element(By.XPATH, self.domov_button_xpath))
        self.nadzorna_plosca_button = Button(self.find_element(By.XPATH, self.nadzorna_plosca_button_xpath))
        self.moji_predmeti_button = Button(self.find_element(By.XPATH, self.moji_predmeti_button_xpath))