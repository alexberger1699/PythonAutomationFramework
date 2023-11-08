import pytest
from autoTests.src.pages.Home_page import Home_page

@pytest.mark.usefixtures('setup')
class Test_end_to_end :


    def test_end_to_end_checkout_guest_user(self):
        home_p = Home_page(self.driver)
        home_p.go_to_home_page()