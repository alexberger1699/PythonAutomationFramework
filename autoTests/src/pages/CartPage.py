
from autoTests.src.pages.locators.RoomCartPageLocator import RoomCartPageLocators
from autoTests.src.SeleniumExtended import SeleniumExtended

class CartPage(RoomCartPageLocators):



    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verifyCartOpen(self):
        self.sl.wait_until_element_is_visible(self.SHOP_BUTTON)

    def click_on_shop_button(self):
        self.sl.wait_and_click(self.SHOP_BUTTON)