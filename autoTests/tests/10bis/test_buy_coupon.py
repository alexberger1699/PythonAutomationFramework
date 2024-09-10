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
        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            # cookie['domain']=".co.il"
            try:
                self.driver.add_cookie(cookie)
                # print(cookie)
            except Exception as e:
                print(e)

        time.sleep(2)
        # Open 10bis credit page
        self.driver.get("https://www.10bis.co.il/next/restaurants/menu/delivery/26698/%D7%A9%D7%95%D7%A4%D7%A8%D7%A1%D7%9C---%D7%9B%D7%9C%D7%9C-%D7%90%D7%A8%D7%A6%D7%99")
        self.driver.maximize_window()
        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            # cookie['domain']=".co.il"
            try:
                self.driver.add_cookie(cookie)
                # print(cookie)
            except Exception as e:
                print(e)
        time.sleep(3)



        # Locators

        def wait_and_click(self, locator, timeout):
            wait(self.driver, timeout).until(locator).click


        # Click on Coupon btn
        time.sleep(7)
        Coupon_btn=self.driver.find_element(By.XPATH,"//*[@id='main-setion']/div[1]/div[1]/section/div/div[2]/div[6]/button/div[2]")
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(Coupon_btn)).click()


        # time.sleep(3)
        # Click on add item btn
        add_item_btn = self.driver.find_element(By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div[3]/div/button/div')
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(add_item_btn)).click()
        # self.driver.find_element(By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div[3]/div/button/div').click()


        # Click on pay button
        add_payment_method_btn = self.driver.find_element(By.XPATH, '//*[@id="shopping-cart-content"]/div[1]/button')
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(add_payment_method_btn)).click()


        # Click on Add payment method
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[contains(text(),"הוספת אמצעי תשלום")]').click()


        # Click on Send order btn
        time.sleep(3)
        # send_order_btn = self.driver.find_element(By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div/div[2]/div[2]/div/div/label/div[2]')
        # wait(self.driver, self.timeout).until(EC.element_to_be_clickable(add_payment_method_btn)).click()
        self.driver.find_element(By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div/div[2]/div[2]/div/div/label/div[2]').click()





        # Click on Send order btn
        time.sleep(3)
        send_order_btn = self.driver.find_element(By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div/div[2]/div[2]/div/div/label/div[2]')
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(send_order_btn)).click()
        # self.driver.find_element(By.XPATH, '//*[@id="modals"]/div/div/div/div/div/div/div[2]/div[2]/div/div/label/div[2]').click()

        # Click on Checkbox payment method for select
        checkbox_of_payment_method = self.driver.find_element(By.XPATH,'//*[@id="modals"]/div/div/div/div/div/div/div[2]/div[2]/div/div')
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(checkbox_of_payment_method)).click()
        # self.driver.find_element(By.XPATH,'//*[@id="modals"]/div/div/div/div/div/div/div[2]/button').click()

        # Click on add btn payment method
        add_btn = self.driver.find_element(By.XPATH,'//*[@id="modals"]/div/div/div/div/div/div/div[2]/button')
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(add_btn)).click()
        # self.driver.find_element(By.XPATH,'//*[@id="modals"]/div/div/div/div/div/div/div[2]/button').click()

        # Click on money amount
        money_amount_field = self.driver.find_element(By.XPATH,"//*[@id='modals']/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]")
        wait(self.driver, self.timeout).until(EC.element_to_be_clickable(money_amount_field)).click()
        # self.driver.find_element(By.XPATH,"//*[@id='modals']/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]").click()


        #Insert amount of money for example 200 shekels
        time.sleep(2)

        # amount_of_money_field = self.driver.find_element(By.XPATH,"//*[@id='modals']/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]")
        # wait(self.driver, self.timeout).until(EC.element_to_be_clickable(amount_of_money_field)).send_keys(200)

        E = self.driver.find_element(By.XPATH,"//*[@id='modals']/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(Keys.ARROW_UP)
        time.sleep(2)
        coupon_amount=200

        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(str(asdc))
        self.driver.find_element(By.XPATH,"//*[@id='modals']/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(Keys.NUMPAD0)
        self.driver.find_element(By.XPATH,"//*[@id='modals']/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(Keys.NUMPAD0)
        # self.driver.find_element(By.XPATH,"//*[@id="modals"]/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(Keys.NUMPAD0)

        time.sleep(555)










