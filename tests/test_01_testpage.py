import time
from distutils.log import log

from base.base_test_case import BaseTestCase
from pages.landing_page import LandingPage
from pages.predstavitev_page import PredstavitevPage


class Test01LandingPage(BaseTestCase):

    def test_01_test(self):
        self.open("https://www.fe.uni-lj.si/sl")
        self.landing_page = LandingPage(self.current_page)
        header = self.landing_page.get_header()
        with header.the_faculty_dropdown as faculty:
            faculty.predstavitev_button.click()
        self.predstavitev_page = PredstavitevPage(self.current_page)
        self.log.info('UUUUAAAAAAAAAAA')
        self.predstavitev_page.toggle_predstavitev.select_option(
            self.predstavitev_page.toggle_predstavitev.POSLANSTVO_IN_VIZIJA
        )
        # time.sleep(2)
        # self.landing_page.navigation_bar.collapse()

        # driv = webdriver.Chrome()
        # driv.get("http://selenium.dev")
