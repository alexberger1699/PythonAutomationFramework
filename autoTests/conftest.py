import os
import time

from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://fuelpoint-qa.roseman.co.il/")
    request.cls.driver = driver


    yield
    driver.close()

    




