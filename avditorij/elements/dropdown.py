import time

from overrides import overrides
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from base.base_page_element import BasePageElement


class Dropdown(BasePageElement):
	def __init__(self, element):
		super().__init__(element)
		self.expand_button_xpath = ...
		self.option_xpath = ...  # './/a[contains(@title, {title})]'

	def expand(self):
		if not self.is_expanded:
			self.click()
			time.sleep(2)
			self.init_expanded()
			self.log.info('Expanding dropdown')

	def collapse(self):
		if self.is_expanded:
			self.click()
			time.sleep(2)
			self.init_collapsed()
			self.log.info('Collapsing dropdown')

	@property
	def is_expanded(self):
		print(f'is displayed: {self.is_displayed()}')
		return self.is_displayed()

	def init_expanded(self):
		pass

	def init_collapsed(self):
		pass

	def get_by_text(self, text):
		assert self.is_expanded, 'Dropdown is not expanded'
		return self.find_element(By.XPATH, self.option_xpath.format(text))

	def __enter__(self):
		self.expand()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.collapse()
		return self


class HeaderDropdown(Dropdown):
	def __init__(self, element):
		super().__init__(element)
		self.menu_level1_xpath = './/span[contains(@class, "menu-level1") and (text()= "{text}")]'
		self.menu_level2_xpath = './/span[contains(@class, "menu-level2") and (text()= "{text}")]'
		self.menu_level3_xpath = './/span[contains(@class, "menu-level3") and (text()= "{text}")]'
		self.menu_level4_xpath = './/span[contains(@class, "menu-level4") and (text()= "{text}")]'

	def __enter__(self):
		self.expand()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		try:
			self.collapse()
		except StaleElementReferenceException:
			self.log.info('Dropdown has already closed automatically')
		return self

	@property
	@overrides
	def is_expanded(self):
		return 'menu-level1-open' in self.get_attribute_or_property('class')

	def get_text(self):
		elems = self.find_elements(By.XPATH, './/span')
		print("LAAAAAAAAAAAAAAAAAAAAAAAa")
		print(len(elems))
		print("[")
		for elem in elems:
			print(f"'{elem.text}',")
		print("]")
