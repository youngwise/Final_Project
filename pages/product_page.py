from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_product_page(self):
        self.should_be_product_added_to_basket()
        self.should_be_product_name_matches_the_name_in_the_basket()
        self.should_be_product_price_matches_the_price_of_the_basket()

    def should_be_product_added_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_TO_BASKET), 'Notification that the product has been added to the basket ' \
                                                         'isn\'t presented '

    def should_be_product_name_matches_the_name_in_the_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert name == name_in_message, 'Product name doesn\'t match the product name in the basket'

    def should_be_product_price_matches_the_price_of_the_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_MESSAGE).text
        assert price == price_in_message, 'Product price doesn\'t match price of the basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_be_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message isn\'t disappeared"
