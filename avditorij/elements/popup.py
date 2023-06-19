from selenium.webdriver.common.by import By

from avditorij.base_elements.base_page_element import BasePageElement


class Popup(BasePageElement):
	def __init__(self, element):
		super().__init__(element)
		self.close_button_xpath = ...
		self.confirm_button_xpath = ...

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.find_element(By.XPATH, self.close_button_xpath).click()
		