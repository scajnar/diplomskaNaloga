from selenium import webdriver
from seleniumbase import DriverContext


class Driver(DriverContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()
