from selenium.webdriver.common.by import By

from base.base_page_element import BasePageElement
from base.page import Page


class DocumentationPage(Page):

    class LeftSidebar(BasePageElement):
        xpath = './/aside[contains(@class, "col-12")]'

        def __init__(self, element):
            super().__init__(element)
            self.overview_text = 'Overview'
            self.overview_xpath = f'.//a/span[contains(text(), "{self.overview_text}")]'

            self.overview = BasePageElement(self.find_element(By.XPATH, self.overview_xpath))

    def __init__(self, driver):
        super().__init__(driver)
        self.left_sidebar = self.LeftSidebar(self.find_element(By.XPATH, self.LeftSidebar.xpath))

