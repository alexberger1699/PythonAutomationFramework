from autoTests.src.pages.locators import MyAccountSinedIOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from autoTests.src.SeleniumExtended import SeleniumExtended
from autoTests.src.helpers.config_helpers import get_base_url

class MyAccountSignedOut(MyAccountSinedIOutLocator):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get('')


    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_btn(self):
        self.sl.wait_and_input_text(self.LOGIN_BTN)
