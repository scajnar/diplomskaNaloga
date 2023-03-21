import time

from base.base_test_case import BaseTestCase
from pages.landing_page import LandingPage


class Test01LandingPage(BaseTestCase):

    def test_01_test(self):
        self.open("http://selenium.dev")
        self.landing_page = LandingPage(self.current_page)
        self.landing_page.navigation_bar.expand()
        self.documentation_page = self.get_documentation_page()
        # self.documentation_page.left_sidebar.overview.click()
        time.sleep(2)
        self.documentation_page.left_sidebar.overview.scroll_to_element()
        self.documentation_page.left_sidebar.overview.highlight()
        # time.sleep(2)
        # self.landing_page.navigation_bar.collapse()

        # driv = webdriver.Chrome()
        # driv.get("http://selenium.dev")
