from selenium.webdriver.common.by import By

from base.web_page import Page
from elements.dropdown import Dropdown


class LandingPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.dropdown_xpath = '//button[contains(@class, "navbar-toggler")]'
        self.navigation_bar = Dropdown(self.find_element(By.XPATH, self.dropdown_xpath))
