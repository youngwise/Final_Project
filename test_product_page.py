from string import ascii_letters, ascii_lowercase, digits
from random import choices
from time import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


# Создадим генератор email и пароля
# Create an email and password generator
def generator_email_and_password():
    """
    Про генератор.

    Генерация строки осуществляется с помощью функции choices() из библиотеки random, которая возвращает массив c размером
    k из случайных элементов определённой последовательности. Последовательность букв и цифр берём из библиотеки string.
    Затем формируем строку, соединяя все символы с помощью join().
    ====================================================================================================================
    About the generator.

     The string is generated using the choices() function from the random library, which returns an array c with size
     k from random elements of a certain sequence. We take the sequence of letters and numbers from the string library.
     Then we form a string by joining all the characters with join().
    """

    # Генерация случайного кол-ва произвольных букв до '@' не меньше 1-го
    # Generating a random number of arbitrary letters up to '@' at least 1
    word_before = choices(ascii_letters, k=int(time() * 1000 % 100//2 + 1))

    # Генерация случайного кол-ва произвольных букв после '@' не меньше 1-го
    # Generating a random number of arbitrary letters after '@' at least 1
    word_after = choices(ascii_lowercase, k=int(time() * 100000 % 100 // 3 + 1))

    # Генерация случайного набора букв и цифр, учитывая, что кол-во символов не менее 9
    # Generating a random set of letters and numbers, given that the number of characters is at least 9
    word_with_digits = choices(ascii_letters + digits, k=int(time() * 1000000 % 100 // 2 + 9))

    email = f'{"".join(word_before)}@{"".join(word_after)}.com'
    password = ''.join(word_with_digits)
    return email, password


class TestUserAddToBasketFromProductPage:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(*generator_email_and_password())
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_basket()
        page.should_be_product_page()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.open_the_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_is_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
