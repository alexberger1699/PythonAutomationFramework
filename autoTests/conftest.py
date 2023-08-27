import os


from selenium import webdriver
import pytest
from autoTests.src import SeleniumExtended as sl
from autoTests.src.pages.locators import loginEvLocators
from autoTests.src.helpers.config_helpers import get_base_url
import time
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    request.cls.driver = driver
    




