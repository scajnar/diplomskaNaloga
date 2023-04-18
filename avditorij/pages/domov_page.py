from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.base_elements.page import Page


class DomovPage(Page):
    def __init__(self, element):
        super().__init__(element)
        self.title_xpath = './/h1'
        self.subtitle_xpath = './/h2'
        self.course_containers_xpath = './/div[contains(@class, "coursebox")]'
        self.course_containers = \
            [self.CourseContainer(x) for x in self.find_elements(By.XPATH, self.course_containers_xpath)]

    class CourseContainer(BasePageElement):
        def __init__(self, element):
            super().__init__(element)
            self.title_xpath = './/h3'
            self.body_xpath = './/p'

