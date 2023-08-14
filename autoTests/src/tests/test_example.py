
from selenium import webdriver


import pytest

pytestmark = [pytest.mark.stan, pytest.mark.raw]
class Test_class:


    @pytest.mark.dd
    def test_a (self):
        print('alex')



    @pytest.mark.dd
    @pytest.mark.smoke
    def test_b(self):
        print('sdd')
        assert 1==2, 'my failed'