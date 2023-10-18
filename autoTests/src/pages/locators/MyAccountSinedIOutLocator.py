from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:


    LOGIN_USERNAME =(By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log in"]')

    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')


    REGISTER_EMAIL_ADDRESS = (By.ID,'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="register"]')
