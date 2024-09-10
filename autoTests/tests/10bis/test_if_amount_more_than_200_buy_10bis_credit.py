import pickle
import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



class TestCoupon():
    driver = webdriver.Chrome()
    timeout=15
    # Locators

    def test_t(self, timeout=15):


        self.driver.get("https://10bis.co.il")
        self.driver.maximize_window()
        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            # cookie['domain']=".co.il"
            try:
                self.driver.add_cookie(cookie)
                # print(cookie)
            except Exception as e:
                print(e)

        time.sleep(222)