from autoTests.src.pages.locators import MyAccountSinedIOutLocator


class MyAccountSignedOut(MyAccountSinedIOutLocator):

    def __init__(self, driver):
        self.driver = driver
    def go_to_my_account(self):
        pass

    def input_login_username(self):
        self.driver.find_element('id', self.login_field)

    def input_login_password(self):
        pass

    def click_login_button(self):
        pass

