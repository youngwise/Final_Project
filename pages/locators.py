from selenium.webdriver.common.by import By


class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main > .price_color')

    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
    PRICE_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')

    MESSAGE_ADD_TO_BASKET = (By.CLASS_NAME, 'alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET = (By.CSS_SELECTOR, '.basket-mini .btn')


class BasketPageLocators:
    ITEMS = (By.CLASS_NAME, 'basket-items')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')

