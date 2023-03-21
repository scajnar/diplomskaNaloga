from base.base_web_page_element import BasePageElement


# class Dropdown(WebPageElement):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.expand_button_xpath = '/html/body/header/nav/button'
#         self.option_xpath = './/a[contains(@title, {title})]'
#         self.about_text = 'About'
#         self.downloads_text = 'Downloads'
#         self.documentation_text = 'Documentation'
#         self.about_xpath = f'.//span[contains(text(), "{self.about_text}")]/..'
#
#     def expand(self):
#         if not self.is_expanded:
#             self.find_element(By.XPATH, self.expand_button_xpath).click()
#             # WebDriverWait.until(EC.element_to_be_clickable(self.about_xpath))
#
#     def collapse(self):
#         if self.is_expanded:
#             self.find_element(By.XPATH, self.expand_button_xpath).click()
#
#     @property
#     def is_expanded(self):
#         return self.is_displayed()
#
#     def select_by_text(self, text):
#         assert self.is_expanded, 'Dropdown is not expanded'
#         self.find_element(By.XPATH, self.option_xpath.format(text)).click()
#
#     @override
#     def click(self):
#         super().click()
#

class Dropdown(BasePageElement):
    def __init__(self, element):
        super().__init__(element)
        self.element = element

    def expand(self):
        self.click()
        self.click()
        self.click()
