import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
import time

class TestBurgerConstructor:
    @allure.title("Переход в ленту заказов по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        main_page.click_constructor()
        assert main_page.is_constructor_opened(), "Конструктор не открылся"
          
    @allure.title("Переход в ленту заказов по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.is_order_feed_opened(), "Лента заказов не открылась"
     
    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        time.sleep(5)
        main_page.click_ingredient()
        time.sleep(5)
        assert main_page.is_modal_open(), "Модальное окно не открылось"   
    
    @allure.title("Закрытие модального окна с деталями ингредиента")
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        time.sleep(5)
        main_page.click_ingredient()
        time.sleep(5)
        main_page.close_modal()
        time.sleep(1)
        assert not main_page.is_modal_open(), "Модальное окно не закрылось"
    
    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        time.sleep(5)
        initial_counter = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_constructor()
        time.sleep(5)
        new_counter = main_page.get_ingredient_counter()
        time.sleep(5)
        assert new_counter > initial_counter, \
            f"Счетчик не увеличился."
    