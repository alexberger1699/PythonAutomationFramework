
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from autoTests.src.pages import searchPage
from autoTests.src.SeleniumExtended import SeleniumExtended


import pytest




@pytest.mark.usefixtures("init_driver")
class Test:
    def Atest_s(self):
        self.sl = SeleniumExtended(self.driver)
        #Go to room.com by init_driver and click on cart button
        #room.com will open by Fixture Inint_driver
        #Click on cart buton function
        cart_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class = cart]')
        cart_button.click()

        #Click on element by inheriate WAIT_AND_CLICK_ON_ELEMENT function from class SeleniumExtended
        # self.sl.wait_and_click(self.cart_button)




        # driver = webdriver.Chrome()
        # driver.get("https://google.com")
        # # time.sleep(3)
        # s =driver.find_element(By.ID, 'APjFqb')
        # s.send_keys('Ipgone')
        time.sleep(3)
        # self.driver.get("https://google.com")
        # self.driver.find_element(By.NAME, 'q').send_keys("alex")


