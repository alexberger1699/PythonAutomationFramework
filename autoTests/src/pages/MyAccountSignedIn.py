
from autoTests.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLoacators
from autoTests.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedOutLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def verify_user_id_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BUTTON)