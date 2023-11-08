import pytest
from autoTests.src.pages.Home_page import Home_page

class end_to_end :

    @pytest.mark.usefixtures('init_driver')
    def test_end_to_end_checkout_guest_user(self):
        home_p = Home_page()
        home_p.go_to_home_page()