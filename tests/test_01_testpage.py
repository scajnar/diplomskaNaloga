import time

from base.base_test_case import BaseTestCase
from pages.landing_page import LandingPage


class Test01LandingPage(BaseTestCase):

    def test_01_test(self):
        self.open("https://www.fe.uni-lj.si/en/")
        self.landing_page = LandingPage(self.current_page)
        header = self.landing_page.get_header()
        with header.the_faculty_dropdown as faculty:
            faculty.highlight()
        # time.sleep(2)
        # self.landing_page.navigation_bar.collapse()

        # driv = webdriver.Chrome()
        # driv.get("http://selenium.dev")
