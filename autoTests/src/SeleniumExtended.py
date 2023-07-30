
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SeleniumExtended(MyAccountSinedIOutLocator):

    def __init__(self, driver):
        self.driver= driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator , text , timeout = None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locator)
        ).send_keys(text)

    def wait_and_click(self, locator , text , timeout = None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locator)
        ).click()



