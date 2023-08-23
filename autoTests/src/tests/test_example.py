from selenium import webdriver
from time import sleep


import pytest

def test_my_example():
    driver = webdriver.Chrome()
    url = 'https://yahoo.com'
    driver.get(url)
    sleep(2)
    driver.quit()




def test_example_test():
    driver = webdriver.Chrome()
    url = 'https://google.com'
    driver.get(url)
    sleep(10)