from avditorij.base_elements.base_test_case import BaseTestCase
from avditorij.pages.domov_page import DomovPage
from avditorij.pages.login_page import LoginPage
from avditorij.pages.nadzorna_plosca_page import NadzornaPloscaPage


class Test01(BaseTestCase):

    def test_01_login(self):
        self.open('https://avditorij2022.fri.uni-lj.si/login/index.php')
        login_page = LoginPage(self.current_page)
        with login_page as login:
            login.username_input.send_keys("samocajnar")
            login.password_input.send_keys("Contort-Sternum5-Thigh")
            login.login_button.click()

        nadzorna_plosca = NadzornaPloscaPage(self.current_page)
        nadzorna_plosca.casovnica.naslednjih_x_dni_dropdown.click()
        header = self.get_header()
        header.domov_button.click()
        domov = DomovPage(self.current_page)