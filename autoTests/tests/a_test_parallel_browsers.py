import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "edge"])
def driver(request):


    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Invalid browser name")

    yield driver
    driver.quit()


def test_website_title(driver):
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title