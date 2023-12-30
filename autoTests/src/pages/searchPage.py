
from autoTests.src.pages.locators import SearchPageLocators
from autoTests.src.utilities.BaseTest import BaseTest
from autoTests.src.SeleniumExtended import SeleniumExtended

class searchPage(BaseTest):


    def __init__(self, driver):
        self.driver=driver
        self.locators= self.SearchPageLocators()
        self.sl = SeleniumExtended(self.driver)

    def search(self, search):
        self.wait_and_input_text(self.SEARCH_FIELD, search)
