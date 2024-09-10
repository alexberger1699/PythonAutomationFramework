import time
import pickle
import pytest

from selenium.webdriver.chrome.options import  Options
from selenium import webdriver

# @pytest.mark.usefixtures("setup")
class Test_10bis:


    def test_10bis_credit(self):
        opt= Options()
        opt.add_experimental_option("debuggerAddress", "localhost:8989")
        driver = webdriver.Chrome()

        driver.get("https://10bis.co.il")
        time.sleep(65)

        cookies = driver.get_cookies()

        print(cookies)
        pickle.dump(cookies, open("cookies.pkl", "wb"))