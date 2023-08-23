import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


def test_one_time_rfuling():
        driver = webdriver.Chrome()

        driver.get("http://onetimerefueling.roseman.co.il/he/")
        time.sleep(2)
        user = driver.find_element(By.NAME, 'userName').send_keys('alex')

        time.sleep(1)

        btn1 = driver.find_element(By.XPATH,'/html/body/app-root/obligo-login/div/div/div/div/form/div[2]/button')
        btn1.click()
        time.sleep(1)

        numbeerPlate = driver.find_element(By.NAME,'carNumber')
        numbeerPlate.click()
        time.sleep(1)
        numbeerPlate.send_keys('6100936')
        time.sleep(1)
        # Find the select element.
        select_element = driver.find_element(By.CSS_SELECTOR, "select[aria-label='.form-select-lg example']")
        select_element.click()
        time.sleep(2)

        # Select the value "95".
        select_element.value_of_css_property("6")

        # Check that the value "95" is selected.
        #assert select_element.get_attribute("value") == "6"

        btn2 = driver.find_element(By.XPATH, '/html/body/app-root/obligo-detail/div/div/div/form/div[4]/button')
        btn2.click()
        time.sleep(10)





