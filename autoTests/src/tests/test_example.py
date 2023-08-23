<<<<<<< HEAD
from selenium import webdriver
from time import sleep
=======

from selenium import webdriver
>>>>>>> caef9fd7de7e70c0e4e98e71ff3549defb40856a


import pytest

<<<<<<< HEAD
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
=======

@pytest.mark.usefixtures("init_driver")
class Test_class():

    def test_a (self):
        print('alex')
        self.driver.get('https://google.com')


    def test_b(self):
        print('sdd')
        assert 1==2, 'failed'
>>>>>>> caef9fd7de7e70c0e4e98e71ff3549defb40856a
