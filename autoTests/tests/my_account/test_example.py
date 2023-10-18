
import pytest
from autoTests.src.utilities.BaseTest import BaseTest
from autoTests.src.pages.MyAccountSignedOut import MyAccountSignedOut


class Test_example(BaseTest):

    @pytest.mark.tcid1
    def test_login_none_existing_user(self):
        my_acount = MyAccountSignedOut(self.driver)
        my_acount.input_login_username('admin')
        my_acount.input_login_password('------')
        my_acount.click_login_btn()

        #verify error message

        expected_err = 'Error: The password you entered for the username admin is incorrect. Lost your password?'

        my_acount.wait_until_error_is_displayed(expected_err)

















        # username = self.driver.find_element(By.CSS_SELECTOR, "input[id='username']")
        # password = self.driver.find_element(By.ID, "password")
        # login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[value='Log in']")
        # username.click()
        # username.send_keys("sadsa")
        #
        # password.click()
        # password.send_keys("sadsa")
        #
        # login_btn.click()
        #
        # # time.sleep(1000)
