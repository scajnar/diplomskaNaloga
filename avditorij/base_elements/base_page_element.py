import inspect
import time

from overrides import overrides
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import logging

from base.logger import Logger


class BasePageElement(WebElement):
    def __init__(self, element):
        super().__init__(parent=element._parent, id_=element.id)
        self.log = Logger()

    def scroll_to_element(self):
        """Scrolls to the element."""
        actions = ActionChains(self._parent)
        actions.move_to_element(self).perform()

    def highlight(self, scroll=False):
        if scroll:
            self.scroll_to_element()
        # Execute the JavaScript code to set the border style of the element
        script = "arguments[0].style.border='2px solid red'"
        self._parent.execute_script(script, self)

        # Generate a dynamic filename using the current timestamp
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_path = f'/home/samo/diplomskaNaloga/.tmp/screenshot_{timestamp}.png'
        # screenshot_path = f'../../.tmp/screenshot_{timestamp}.png'
        self._parent.save_screenshot(screenshot_path)

    def wait_for_visibility(self, timeout=10):
        WebDriverWait(self._parent, timeout).until(
            EC.visibility_of_element_located((By.ID, self.id))
        )

    def wait_for_clickable(self, timeout=10):
        WebDriverWait(self._parent, timeout).until(
            EC.element_to_be_clickable((By.ID, self.id))
        )

    def javascript_click(self):
        """Clicks the element using JavaScript. Used when normal click() isn't working as expected."""
        script = "arguments[0].click()"
        self._parent.execute_script(script, self)

    def get_attribute_or_property(self, name):
        return self.get_attribute(name) or self.get_property(name)

    def find_element(self, by=By.ID, value=None, wait=10) -> WebElement:
        # self.log.info(f'Searching for an element with xpath: {value}')
        return super().find_element(by, value)

    @overrides
    def click(self, highlight=False, log=False):
        if highlight:
            self.highlight()
        if log:
            self.log.info(f'Clicking {self.text}')
        super().click()