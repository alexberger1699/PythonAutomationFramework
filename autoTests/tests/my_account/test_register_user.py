
import pytest
from autoTests.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("setup")
class TestRegisterUser:

    @pytest.mark.tcid13
    def test_register_user(self):
        my_account_o = MyAccountSignedOut(self.driver)

        my_account_o.input_register_email('a264@gmail.com')
        my_account_o.input_register_password('1234')
        my_account_o.click_register_btn()


        #verify user registered



