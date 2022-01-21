import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_add_to_basket(self):
        self.product_added_to_basket()
        self.product_name_comprasion()
        self.product_price_comprasion()

    def product_added_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_TO_BASKET), 'Notification that the product has been added to the basket ' \
                                                         'isn\'t presented '

    def product_name_comprasion(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert name == name_in_message, 'Product name doesn\'t match the product name in the basket'

    def product_price_comprasion(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_MESSAGE).text
        assert price == price_in_message, 'Product price doesn\'t match price basket'
