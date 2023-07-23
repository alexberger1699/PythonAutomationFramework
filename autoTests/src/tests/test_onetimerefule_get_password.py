import time

from selenium.webdriver.common.by import By

import pytest

@pytest.mark.usefixtures("init_driver")
class TestExample():

    def test_login(self):
        import pdb;
        self.driver.get("http://onetimerefueling.roseman.co.il/he/#/login")
        user = self.driver.find_element(By.NAME,'userName').send_keys('alex')
        btn = self.driver.find_element(By.XPATH, '/html/body/app-root/obligo-login/div/div/div/div/form/div[2]/button').click()
        pdb.set_trace()




