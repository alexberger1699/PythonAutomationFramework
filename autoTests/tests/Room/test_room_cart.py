import time

from selenium.webdriver.common.by import By
from autoTests.src.pages import searchPage
from autoTests.src.SeleniumExtended import SeleniumExtended
import pytest

from autoTests.src.pages.CartPage import CartPage
from autoTests.src.pages.RoomPage import RoomPage


@pytest.mark.usefixtures("init_driver")
class Test:

    def test_s(self):
        self.sl = SeleniumExtended(self.driver)
        room_page = RoomPage(self.driver)
        cart_page = CartPage(self.driver)
        # Go to room.com by init_driver and click on cart button
        # room.com will open by Fixture Inint_driver
        # Click on cart buton function
        room_page.click_on_cart_button()
        time.sleep(2)


        #Validate YOUR CART title
        cart_page.verifyCartOpen()
        time.sleep(2)
        #Open cart
        cart_page.click_on_shop_button()
