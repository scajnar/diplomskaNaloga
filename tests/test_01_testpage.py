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
        with header.o_fakulteti_dropdown as faculty:
            #faculty.predstavitev_button.highlight()
            #faculty.predstavitev_button.click(log=True)
            faculty.fakulteta_button.highlight()
            faculty.habilitacije_button.highlight()
            time.sleep(10)
            # faculty.predstavitev_button.click()
        # with header.o_fakulteti_dropdown as drp:
        #     drp.zalozba_in_trgovina_button.click(highlight=True)
