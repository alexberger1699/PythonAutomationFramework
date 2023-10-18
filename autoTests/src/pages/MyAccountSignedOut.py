from autoTests.src.pages.locators.MyAccountSinedIOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from autoTests.src.SeleniumExtended import SeleniumExtended
from autoTests.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)




    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    # def primitive_input_login_username(self, username):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.LOGIN_USERNAME)
    #     ).sendkeys(username)
    #
    #
    #
    # def primitive_input_password(self, password):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.LOGIN_PASSWORD)
    #     ).sendkeys(password)
    #
    # def primitive_input_login_username(self, LOGIN_BTN):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.LOGIN_BTN)
    #     ).click()



    def input_login_username(self, username):
        logger.debug(f'input username {username}')

        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_btn(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_elemment_contains_text(self.ERRORS_UL, exp_err)




    def input_register_email(self, reg_email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL_ADDRESS, reg_email)

    def input_register_password(self, reg_password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, reg_password)

    def click_register_btn(self):
        self.sl.wait_and_click(self.REGISTER_BUTTON)
