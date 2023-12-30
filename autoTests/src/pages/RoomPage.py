from autoTests.src.SeleniumExtended import SeleniumExtended
from autoTests.src.pages.locators.RoomCartPageLocator import  RoomCartPageLocators


class RoomPage(RoomCartPageLocators):

    def __init__(self, driver):
        self.driver=driver
        self.sl = SeleniumExtended(self.driver)


    def click_on_cart_button(self):
        self.sl.wait_and_click(self.CART_BUTTON)


