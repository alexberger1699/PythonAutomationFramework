import time

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "edge"])
def driver(request):

    #
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Invalid browser name")

    #Close driver
    yield driver
    driver.quit()


def test_website_title(driver):
    driver.get("https://www.example.com")
    time.sleep(7)
    #Check title
    assert "Example Domain" in driver.title