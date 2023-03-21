import time

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase, Driver
from selenium import webdriver

from pages.documentation_page import DocumentationPage


class BaseTestCase(BaseCase):
    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome()
        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>

    def tearDown(self):
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot"
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            # <<< Run custom code if the test passed. >>>
            pass
        # (Wrap unreliable tearDown() code in a try/except block.)
        # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
        time.sleep(2)
        self.driver.quit()
        super().tearDown()

    def login(self):
        # <<< Placeholder. Add your code here. >>>
        # Reduce duplicate code in tests by having reusable methods like this.
        # If the UI changes, the fix can be applied in one place.
        pass

    def example_method(self):
        # <<< Placeholder. Add your code here. >>>
        pass

    @property
    def current_page(self):
        return self.driver.find_element(By.XPATH, '/html/body')

    def get_documentation_page(self):
        link = 'https://www.selenium.dev/documentation/'
        self.open(link)
        return DocumentationPage(self.current_page)