from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    login_username =(By.ID, 'username')
    login_password = (By.ID, 'password')
    login_btn = (By.ID, 'button')