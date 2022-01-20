from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


# обработчик, который считывает из командной строки параметр language
# handler that reads the language parameter from the command line
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


# реализация логики запуска браузера с указанным языком пользователя
# implementation of the browser launch logic with the specified user language
@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')

    # проверка, что параметр language указан
    # checking that the language parameter is specified
    if language is None:
        raise pytest.UsageError('--language should be don\'t None!')

    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': language})

    print('\nStart browser for test...')
    browser = webdriver.Chrome(options=option)
    browser.implicitly_wait(5)
    yield browser
    print('\nquit browser...')
    browser.quit()
