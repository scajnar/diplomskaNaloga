from overrides import overrides
from selenium.webdriver.common import log
from selenium.webdriver.common.by import By

from base.base_web_page_element import BasePageElement
from elements.button import Button
from elements.dropdown import HeaderDropdown


class Header(BasePageElement):

    def get_the_faculty_dropdown(self):
        return self.TheFacultyDropdown(self.find_element(By.XPATH, self.TheFacultyDropdown.xpath))

    class TheFacultyDropdown(HeaderDropdown):
        # xpath = './/ul[contains(@class, "menu-level2") and contains(@style, "display: block")]'

        def __init__(self, element):
            super().__init__(element)
            self.the_faculty_text = 'The Faculty'
            # self.expand_button_xpath = f'//span[contains(@class, "menu-level1") and contains(text(), "{self.the_faculty_text}")]'
            # self.expand_button_xpath = f'{self.xpath}/parent::li'
            self.parent_xpath = '../..'
            self.about_faculty_text = 'About Faculty'

            self.about_faculty_xpath = f'.//span[contains(@class, "menu-level2") and (text()= "{self.about_faculty_text}")]'

            self.about_faculty: 'Button' = ...

        def init_expanded(self):
            self.about_faculty_button = Button(self.find_element(By.XPATH, self.about_faculty_xpath))

        def init_collapsed(self):
            self.about_faculty = None



    class EducationDropdown(HeaderDropdown):
        def __init__(self, element):
            super().__init__(element)

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
        self.the_faculty_text = 'The Faculty'
        self.education_text = 'Education'
        self.research_text = 'Research'
        self.news_text = 'News'
        self.covid_19_info_text = 'COVID-19 info'

        self.the_faculty_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.the_faculty_text}")]/ancestor::li'
        self.education_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.education_text}")]/ancestor::li'
        self.research_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.research_text}")]/ancestor::li'
        self.news_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.news_text}")]/ancestor::li'
        self.covid_19_info_xpath = f'.//span[contains(@class, "menu-level1") and contains(text(), "{self.covid_19_info_text}")]/ancestor::li'

        self.the_faculty_dropdown = self.TheFacultyDropdown(self.find_element(By.XPATH, self.the_faculty_xpath))
        self.education_button = Button(self.find_element(By.XPATH, self.education_xpath))
        self.research_button = Button(self.find_element(By.XPATH, self.research_xpath))
        self.news_button = Button(self.find_element(By.XPATH, self.news_xpath))
        self.covid_19_info_button = Button(self.find_element(By.XPATH, self.covid_19_info_xpath))