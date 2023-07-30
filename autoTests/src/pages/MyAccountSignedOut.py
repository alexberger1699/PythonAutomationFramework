from autoTests.src.pages.locators import MyAccountSinedIOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MyAccountSignedOut(MyAccountSinedIOutLocator):

    def __init__(self, driver):
        self.driver = driver
    def go_to_my_account(self):
        self.driver.get('')

    def input_login_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_username)
        ).send_keys(username)

    def input_login_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_password)
        ).send_keys(password)

    def click_login_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_btn)
        ).click()
