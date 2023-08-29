import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from autoTests.src.SeleniumExtended import SeleniumExtended
from autoTests.src.utilities.BaseTest import BaseTest


class Test_example(BaseTest):


    def test_login_none_existing_user(self):
        username = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/input")
        password = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div[2]/div[2]/input")
        login_btn = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div[2]/div[6]/button[2]")

        username.click()
        username.send_keys("sadsa")

        password.click()
        password.send_keys("sadsa")

        login_btn.click()

        time.sleep(1000)
