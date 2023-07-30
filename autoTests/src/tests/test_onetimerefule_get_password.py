import time

from selenium.webdriver.common.by import By
from autoTests.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

@pytest.mark.usefixtures("init_driver")
class TestExample(SeleniumExtended):



    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10
        self.sl = SeleniumExtended(self.driver)



    def test_login(self):
        import pdb;
        self.driver.get("http://onetimerefueling.roseman.co.il/he/#/login")
        user = self.sl.wait_and_input_text(By.NAME,'userName','lex')#self.driver.find_element(By.NAME,'userName').send_keys('alex')
        btn = self.driver.find_element(By.XPATH, '/html/body/app-root/obligo-login/div/div/div/div/form/div[2]/button').click()
        pdb.set_trace()




