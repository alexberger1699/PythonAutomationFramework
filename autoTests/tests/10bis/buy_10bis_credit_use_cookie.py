import pickle
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET


class TestTen10bis:

    def test10BisCredit(self):
        driver = webdriver.Chrome()
        driver.get("https://10bis.co.il")
        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            # cookie['domain']=".co.il"
            try:
                driver.add_cookie(cookie)
                # print(cookie)
            except Exception as e:
                print(e)

        # time.sleep(2)
        timeout = 15
        # Open 10bis credit page
        driver.get("https://www.10bis.co.il/next/user-report?dateBias=0")
        driver.maximize_window()

        time.sleep(4)
        # Get cerdit amount before purchase credit


        credit_amount_before_purchase = driver.find_element(By.CSS_SELECTOR,'span[class="PrepaidCard__Balance-sc-1yb9170-4 cVseMg"]')
        text_include_unnecessary_symbols = credit_amount_before_purchase.text.replace('₪', '')
        text_of_available_amount = float(text_include_unnecessary_symbols)
        avalable_amount = int(text_of_available_amount)
        print(avalable_amount)
        if 41 < avalable_amount:
           print('<<<<<<<<<<<<<<<<<GREAT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        else:
            print('++++++++++++++++++++ERROR++++++++++++++++++++++++++++++++')


        time.sleep(222)
        # Click on CREDIT button
        credit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'הטענת תן ביס קרדיט')]")
        credit_btn.click()
        # wait(driver, timeout).until(EC.element_to_be_clickable(credit_btn))
        time.sleep(4)
        # Approve Credit purchase by click CONTINUE/המשך button on Credit popup
        continiue_btn = driver.find_element(By.XPATH, '//button[contains(text(), "המשך")]')
        continiue_btn.click()
        time.sleep(2)

        continiue_btn = driver.find_element(By.XPATH, '//button[contains(text(), "הטענת קרדיט")]')
        continiue_btn.click()
        time.sleep(5)
