from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.base_elements.page import Page
from avditorij.elements.info_icon import InfoIcon


class DomovPage(Page):
    def __init__(self, element):
        super().__init__(element)
        self.title_xpath = './/h1'
        self.subtitle_xpath = './/h2'
        self.course_containers_xpath = './/div[contains(@class, "coursebox")]'
        # self.course_containers = \
        #     [self.CourseContainer(x) for x in self.find_elements(By.XPATH, self.course_containers_xpath)]

    class CourseContainer(BasePageElement):
        def __init__(self, element):
            super().__init__(element)
            self.title_xpath = './/h3'
            self.body_xpath = './/p'
            self.lock_icon_xpath = './/div[@class="enrolmenticons"]/i[contains(@class, "fa-unlock-alt")]'
            self.sign_in_icon_xpath = './/div[@class="enrolmenticons"]/i[contains(@class, "fa-sign-in")]'
            self.key_icon_xpath = './/div[@class="enrolmenticons"]/i[contains(@class, "fa-key")]'

            self.title = self.find_element(By.XPATH, self.title_xpath)
            # self.body = self.find_element(By.XPATH, self.body_xpath)

            # self.key_icon = InfoIcon(self.find_auxiliary_element(By, self.key_icon_xpath))
            self.sign_in_icon_xpath = InfoIcon(self.find_auxiliary_element(By, self.sign_in_icon_xpath))
            self.lock_icon_xpath = InfoIcon(self.find_auxiliary_element(By, self.lock_icon_xpath))

