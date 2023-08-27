
import time

from selenium import webdriver
import pytest
from autoTests.src import SeleniumExtended as sl
from autoTests.src.pages.locators import loginEvLocators
from autoTests.src.helpers.config_helpers import get_base_url
from autoTests.src.utilities import BaseTest
class Test_example():



    def test_login(self):
        print("test")
        # browser = get_base_url()
        # self.driver.get(browser)
        # sl.wait_and_click(self.USERNAME)



