
from selenium import webdriver


import pytest


@pytest.mark.usefixtures("init_driver")
class Test_class():

    def test_a (self):
        print('alex')
        self.driver.get('https://google.com')


    def test_b(self):
        print('sdd')
        assert 1==2, 'failed'