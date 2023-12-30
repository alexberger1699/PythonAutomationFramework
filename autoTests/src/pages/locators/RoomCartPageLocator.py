from selenium.webdriver.common.by import By

class RoomCartPageLocators:


    CART_BUTTON = (By.CSS_SELECTOR, 'button[class = cart]')
    SHOP_BUTTON = (By.CSS_SELECTOR, '#cart-sidebar-empty > div:nth-child(2) > a')