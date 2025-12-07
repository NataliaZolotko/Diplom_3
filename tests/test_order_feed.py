import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedLocators
import time

class TestOrderFeed:
    @allure.title("Увеличение счетчика 'Выполнено за всё время' при создании нового заказа")
    def test_total_orders_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.authorization()
        time.sleep(3)
        main_page.click_order_feed()
        time.sleep(10)
        order_feed_page = OrderFeedPage(driver)
        initial_total_orders = order_feed_page.get_total_orders_count()
        main_page.click_constructor()
        time.sleep(3)
        main_page.add_ingredient_to_constructor()
        time.sleep(3)
        order_number = order_feed_page.place_an_order_and_get_number()
        time.sleep(10)
        main_page.close_modal()
        main_page.click_order_feed()
        time.sleep(60)
        new_total_orders = order_feed_page.get_total_orders_count()
        assert new_total_orders > initial_total_orders, \
                    f"Счетчик 'Выполнено за всё время' не увеличился. Было: {initial_total_orders}, стало: {new_total_orders}"
   
   
    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании нового заказа")
    def test_today_orders_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.authorization()
        time.sleep(3)
        main_page.click_order_feed()
        time.sleep(10)
        order_feed_page = OrderFeedPage(driver)
        initial_today_orders = order_feed_page.get_today_orders_count()
        main_page.click_constructor()
        time.sleep(3)
        main_page.add_ingredient_to_constructor()
        time.sleep(3)
        order_number = order_feed_page.place_an_order_and_get_number()
        time.sleep(10)
        main_page.close_modal()
        main_page.click_order_feed()
        time.sleep(30)
        new_today_orders = order_feed_page.get_today_orders_count()
        assert new_today_orders > initial_today_orders, \
                    f"Счетчик 'Выполнено за всё время' не увеличился. Было: {initial_today_orders}, стало: {new_today_orders}"
    
    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")    
    def test_orders_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.authorization()
        time.sleep(3)
        order_feed_page = OrderFeedPage(driver)
        main_page.add_ingredient_to_constructor()
        time.sleep(3)
        #order_feed_page.place_an_order()
        order_number = order_feed_page.place_an_order_and_get_number_without_waiting()
        time.sleep(2)
        main_page.close_modal()
        main_page.click_order_feed()
        time.sleep(20)
        order_in_progress = order_feed_page.get_orders_in_progress()
        assert order_number in order_in_progress, \
           f"Заказ {order_number} не найден в списке 'В работе'. Список: {order_in_progress}"