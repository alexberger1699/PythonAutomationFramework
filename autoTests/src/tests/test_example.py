


from selenium import webdriver
import pytest
from autoTests.src import SeleniumExtended as sl
from autoTests.src.pages.locators import loginEvLocators
from autoTests.src.helpers.config_helpers import get_base_url

class Test_example:

    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    def login(self):
        browser = get_base_url()
        self.driver.get(browser)
        sl.wait_and_click(self.USERNAME)