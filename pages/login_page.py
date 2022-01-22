from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Login url is incorrect'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form isn\'t presented'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form isn\'t presented'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        for i in range(1, 3):
            input_password = self.browser.find_element(
                LoginPageLocators.REGISTER_PASSWORD[0], LoginPageLocators.REGISTER_PASSWORD[1]+str(i))
            input_password.send_keys(password)
        registering = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registering.click()
