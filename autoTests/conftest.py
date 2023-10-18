import os
import time

from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'firefox', 'edge']

    browser = os.environ.get('BROWSER', None)


    if not browser:
        raise Exception("The envoronment variable 'BROWSER' must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser {browser} is not one of the supporteds."
                        f"Supported are {supported_browsers}")


    if browser in ('chrome'):
        driver = webdriver.Chrome()
    elif browser in('firefox'):
        driver = webdriver.Firefox()
    elif browser in ('edge'):
        driver = webdriver.Edge()




@pytest.fixture(scope="class")
def setup(request):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.headless = True
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    #Headless mode run tests
    # driver = webdriver.Chrome(options=chrome_options)

    #GUI mode run tests
    driver = webdriver.Chrome(options=options)

    #URL
    #driver.get("https://fuelpoint-qa.roseman.co.il/")
    driver.get("http://localhost:8888/quicksite/my-account/")


    request.cls.driver = driver


    # yield
    # driver.close()

    




