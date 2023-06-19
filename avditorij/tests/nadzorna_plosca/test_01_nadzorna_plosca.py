from avditorij.base_elements.base_test_case import BaseTestCase
from avditorij.pages.domov_page import DomovPage
from avditorij.pages.login_page import LoginPage
from avditorij.pages.nadzorna_plosca_page import NadzornaPloscaPage
import logging as log

class Test01(BaseTestCase):

	def setUp(self):
		super().setUp()
		self.open('https://avditorij2022.fri.uni-lj.si/login/index.php')
		login_page = LoginPage(self.current_page)
		with login_page as login:
			login.username_input.send_keys("samocajnar")
			login.password_input.send_keys("Contort-Sternum5-Thigh")
			login.login_button.click()


	def test_02_assert_casovnica_is_present(self):
		nadzorna_plosca = NadzornaPloscaPage(self.current_page)
		assert nadzorna_plosca.casovnica, "Casovnica couldn't be located"
		self.log.info('Casovnica is present, as expected.')
		nadzorna_plosca.casovnica.highlight()


	def test_03_assert_casovnica_elements_are_present(self):
		nadzorna_plosca = NadzornaPloscaPage(self.current_page)
		nadzorna_plosca.casovnica.naslednjih_x_dni_dropdown.highlight()
		self.log.info('Naslednjih x dni dropdown is present')
		nadzorna_plosca.casovnica.razvrsti_po_dropdown.highlight()
		self.log.info('Naslednjih razvrsti po dropdown is present')
		nadzorna_plosca.casovnica.search_input.highlight()
		self.log.info('Casovnica input is present')

	def test_04_assert_koledar_is_present(self):
		nadzorna_plosca = NadzornaPloscaPage(self.current_page)
		nadzorna_plosca.koledar.highlight()
		self.log.info('Koledar is present')
		assert nadzorna_plosca.koledar.predmeti_dropdown, 'Predmeti dropdown is not present'
		nadzorna_plosca.koledar.predmeti_dropdown.highlight()
		self.log.info('Predmeti dropdown is present')

		assert nadzorna_plosca.koledar.nov_dogodek_button, 'Nov dogodek button is not present'
		self.log.info('Nov dogodek button is present')
		nadzorna_plosca.koledar.nov_dogodek_button.highlight()

		assert nadzorna_plosca.koledar.next_month_button, 'Next month button is not present'
		self.log.info('Next month button is present')
		nadzorna_plosca.koledar.next_month_button.highlight()

		assert nadzorna_plosca.koledar.previous_month_button, 'Previous month button is not present'
		self.log.info('Previous month button is present')
		nadzorna_plosca.koledar.previous_month_button.highlight()

		assert nadzorna_plosca.koledar.full_calendar_button, 'Full calendar button is not present'
		self.log.info('Full calendar button is present')
		nadzorna_plosca.koledar.full_calendar_button.highlight()

		assert nadzorna_plosca.koledar.upravljanje_narocnin_button, 'Upravljanje narocnin button is not present'
		self.log.info('Upravljanje narocnin button is present')
		nadzorna_plosca.koledar.upravljanje_narocnin_button.highlight()

	def test_05_assert_koledar_days_are_present(self):
		nadzorna_plosca = NadzornaPloscaPage(self.current_page)
		for day in nadzorna_plosca.koledar.calendar_days:
			day.highlight()
		self.log.info('Koledar days are present')

	def test_06_assert_naslednje_x_mesece_dropdown_expands(self):
		nadzorna_plosca = NadzornaPloscaPage(self.current_page)
		with nadzorna_plosca.casovnica.naslednjih_x_dni_dropdown as dropdown:
			dropdown.get_by_text(dropdown.naslednjih_6_mesecev_text).highlight()

	def test_07_assert_nov_dogodek_popup_opens(self):
		nadzorna_plosca = NadzornaPloscaPage(self.current_page)
		nadzorna_plosca.koledar.nov_dogodek_button.click()


