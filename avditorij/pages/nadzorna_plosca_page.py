from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement
from avditorij.base_elements.page import Page
from avditorij.elements.button import Button
from avditorij.elements.dropdown import Dropdown
from avditorij.elements.input import Input, DatumInput
from avditorij.elements.popup import Popup



class NadzornaPloscaPage(Page):
	def __init__(self, element):
		super().__init__(element)
		self.casovnica_text = "Časovnica"
		self.koledar_text = "Koledar"
		self.casovnica_xpath = f'.//h5[text()="{self.casovnica_text}"]/parent::div[contains(@class, "card-body")]'
		self.koledar_xpath = f'.//h5[text()="{self.koledar_text}"]/parent::div[contains(@class, "card-body")]'

		self.casovnica = self.Casovnica(self.find_element(By.XPATH, self.casovnica_xpath))
		self.koledar = self.Koledar(self.find_element(By.XPATH, self.koledar_xpath))

	class Casovnica(BasePageElement):
		def __init__(self, element):
			super().__init__(element)
			self.title_xpath = './/h5'
			self.naslednjih_x_dni_dropdown_xpath = \
				'.//span[contains(@id, "timeline-day")]/ancestor::div[contains(@class, "dropdown")]'
			self.razvrsti_po_dropdown_xpath = \
				'.//span[contains(@id, "timeline-view")]/ancestor::div[contains(@data-region, "view-selector")]'
			self.search_input_xpath = './/input[@id="searchinput"]'

			self.naslednjih_x_dni_dropdown = self.NaslednjihXDniDropdown(self.find_element(By.XPATH, self.naslednjih_x_dni_dropdown_xpath))
			self.razvrsti_po_dropdown = Dropdown(self.find_element(By.XPATH, self.razvrsti_po_dropdown_xpath))
			self.search_input = Input(self.find_element(By.XPATH, self.search_input_xpath))

		class NaslednjihXDniDropdown(Dropdown):
			def __init__(self, element):
				super().__init__(element)
				self.vse_text = 'Vse'
				self.poteklo_text = 'Poteklo'
				self.naslednjih_7_dni_text = 'Naslednjih 7 dni'
				self.naslednjih_30_dni_text = 'Naslednjih 30 dni'
				self.naslednje_3_mesece_text = 'Naslednje 3 mesece'
				self.naslednjih_6_mesecev_text = 'Naslednjih 6 mesecev text'

				self.option_xpath = './/a[contains(@class, "dropdown-item") and contains(text(), "{text}")]'
				# self.naslednjih_6_mesecev_option_xpath = self.option_xpath.format('text', self.naslednjih_6_mesecev_text)

	class Koledar(BasePageElement):
		def __init__(self, element):
			super().__init__(element)
			self.full_calendar_button_text = 'Full calendar'
			self.upravljanje_narocnin_button_text = 'Upravljanje naročnin'

			self.title_xpath = './/h5'
			self.predmeti_dropdown_xpath = './/select[contains(@id, "calendar-course")]'
			self.nov_dogodek_button_xpath = './/button[@data-action="new-event-button"]'
			self.current_date_text_xpath = './/h4[@class="current"]'
			self.previous_month_button_xpath = './/a[@class="arrow_link previous"]'
			self.next_month_button_xpath = './/a[@class="arrow_link next"]'
			self.calendar_days_xpath = './/td[@data-region="day"]'
			self.full_calendar_button_xpath = f'.//a[contains(text(), "{self.full_calendar_button_text}")]'
			self.upravljanje_narocnin_button_xpath = f'.//a[contains(text(), "{self.upravljanje_narocnin_button_text}")]'

			self.title = self.find_element(By.XPATH, self.title_xpath)
			self.predmeti_dropdown = Dropdown(self.find_element(By.XPATH, self.predmeti_dropdown_xpath))
			self.nov_dogodek_button = Button(self.find_element(By.XPATH, self.nov_dogodek_button_xpath))
			self.previous_month_button = Button(self.find_element(By.XPATH, self.previous_month_button_xpath))
			self.next_month_button = Button(self.find_element(By.XPATH, self.next_month_button_xpath))
			self.full_calendar_button = Button(self.find_element(By.XPATH, self.full_calendar_button_xpath))
			self.upravljanje_narocnin_button = \
				Button(self.find_element(By.XPATH, self.upravljanje_narocnin_button_xpath))
			self.calendar_days = [self.CalendarDay(x) for x in self.find_elements(By.XPATH, self.calendar_days_xpath)]

		def get_nov_dogodek_popup(self):
			return self.NovDogodekPopup(self.find_element(By.XPATH, self.NovDogodekPopup.xpath))

		class CalendarDay(BasePageElement):
			def __init__(self, element):
				super().__init__(element)

		class NovDogodekPopup(Popup):
			xpath = '//div[contains(@class, "modal-content")]'
			def __init__(self, element):
				super().__init__(element)
				self.naslov_dogodka_input_xpath = './/div[contains(@id, "fitem_id_name")]//input'
				self.datum_input_xpath = './/div[contains(@id, "fitem_id_timestart")]//fieldset'
				self.tip_dogodka_dropdown_xpath = './/div[contains(@id, "fitem_id_eventtype")]//select'
				self.prikazi_vec_button_xpath = './/div[contains(@class, "fitem moreless-actions")]//a'

				self.opis_input_xpath = './/div[contains(@id, "fitem_id_description")]//div' \
				                        '[contains(@id, "id_descriptioneditable")]'
				self.lokacija_input_xpath = './/div[contains(@id, "fitem_id_location")]//input'
				self.trajanje_settings_xpath = './/div[contains(@id, "fgroup_id_durationgroup")]//fieldset'
				self.ponovi_ta_dogodek_checkbox_xpath = ...
				self.ponovi_tedensko_input_xpath = './/div[contains(@id, "fitem_id_repeats")]//input'
				self.confirm_button_xpath = './/div[contains(@class, "modal-footer")]//button'
				self.shrani_button_xpath = self.confirm_button_xpath
				self.close_button_xpath = './/div[contains(@class, "modal-header")]//button'

				self.naslov_dogodka_input = Input(self.find_element(By.XPATH, self.naslov_dogodka_input_xpath))
				self.datum_input = DatumInput(self.find_element(By.XPATH, self.datum_input_xpath))
				self.tip_dogodka_dropdown = Dropdown(self.find_element(By.XPATH, self.tip_dogodka_dropdown_xpath))

			def is_expanded(self):
				return 'true' in self.find_element(By.XPATH, self.prikazi_vec_button_xpath).get_attribute('aria-expanded')

			def init_expanded(self):
				assert self.is_expanded(), '"Prikazi vec" is not expanded'
				self.opis_input = Input(self.find_element(By.XPATH, self.opis_input_xpath))
				self.lokacija_input = Input(self.find_element(By.XPATH, self.lokacija_input_xpath))
				self.trajanje_settings_xpath = self.TrajanjeSettings(self.find_element(By.XPATH, self.trajanje_settings_xpath))
				self.ponovi_tedensko_input = Input(self.find_element(By.XPATH, self.ponovi_tedensko_input_xpath))

			class TrajanjeSettings(BasePageElement):
				def __init__(self, element):
					super().__init__(element)
					self.brez_trajanja_radio_button_xpath = './/input[contains(@id, "id_duration_0")]'
					self.do_radio_button_xpath = './/input[contains(@id, "id_duration_1")]'
					self.trajanje_v_minutah_radio_button_xpath = './/input[contains(@id, "id_duration_2")]'
					self.trajanje_v_minutah_input = './/input[contains(@id, "id_timedurationminutes")]'
