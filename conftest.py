import pytest
from selenium import webdriver
from data import *



@pytest.fixture(scope="function", params=['firefox','chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.get(main_site)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    