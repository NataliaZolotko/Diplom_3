from pages.base_page import BasePage
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from locators.basic_function_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import time
import re


class OrderFeedPage(BasePage):
    @allure.step("Проверить, что открыта лента заказов")
    def is_order_feed_opened(self):
        return self.is_element_visible(OrderFeedLocators.PAGE_TITLE)
    
    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_order_feed_loaded(self, timeout=20):
        self.wait_for_visible(OrderFeedLocators.PAGE_TITLE, timeout)
       
    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        text = self.get_element_text(OrderFeedLocators.TODAY_ORDERS_COUNT,timeout=10)
        if not text:
            raise ValueError("Элемент найден, но текст пустой") 
        match = re.search(r'\d+', text)
        if match:
            return int(match.group())
        else:
            raise ValueError(f"Не удалось извлечь число из текста: '{text}'")  
        
    @allure.step("Получить количество выполненных заказов за все время")
    def get_total_orders_count(self):
        text = self.get_element_text(OrderFeedLocators.TOTAL_ORDERS_COUNT,timeout=10)
        if not text:
            raise ValueError("Элемент найден, но текст пустой") 
        match = re.search(r'\d+', text)
        if match:
            return int(match.group())
        else:
            raise ValueError(f"Не удалось извлечь число из текста: '{text}'")       
            
    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        try:
            elements = self.find_elements(OrderFeedLocators.NUMBER_ORDER_AT_WORK, timeout=10)
            orders = []
            for element in elements:
                text = element.text.strip()
                if text:
                    if text.startswith('0'):
                        text = text.lstrip('0')
                    orders.append(text)
            return orders
        except:
            return []
            
    @allure.step("Кликнуть на кнопку Оформить заказ")
    def place_an_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)
        self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=20)
    
    @allure.step("Оформляем заказ с получением номера")
    def place_an_order_and_get_number(self):
        self.click(MainPageLocators.ORDER_BUTTON)
        modal_window = self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=10)
        order_number_element = self.wait_for_visible(OrderFeedLocators.NUMBER_ORDER, timeout=30)       
        def wait_for_real_order_number(driver):
            try:
                order_element = driver.find_element(*OrderFeedLocators.NUMBER_ORDER)
                order_text = order_element.text
                match = re.search(r'\d+', order_text)
                if match:
                    order_num = match.group()
                    return order_num != "9999"
                return False
            except:
                return False
        WebDriverWait(self.driver, 20).until(wait_for_real_order_number) 
        order_number_text = order_number_element.text
        match = re.search(r'\d+', order_number_text)
        if match:
            order_number = match.group()
            if order_number == "9999":
                all_elements = self.driver.find_elements(*OrderFeedLocators.NUMBER_ORDER)
                for element in all_elements:
                    text = element.text
                    match = re.search(r'\d+', text)
                    if match and match.group() != "9999":
                        return match.group()
        else:
            order_number = order_number_text
        return order_number
    
    @allure.step("Ждем появления конкретного заказа в разделе 'В работе'")
    def wait_for_specific_order_in_progress(self, order_number, timeout=80):
        if not order_number:
            raise ValueError("Не передан номер заказа для ожидания")
        def is_order_in_elements(driver):
            try:
                elements = driver.find_elements(*OrderFeedLocators.NUMBER_ORDER_AT_WORK)
                for element in elements:
                    text = element.text.strip()
                    if text:
                        if order_number in text:
                            return True                
                return False
            except Exception as e:
                return False
        try:
            WebDriverWait(self.driver, timeout).until(is_order_in_elements)
            return True   
        except TimeoutException:
            print(f"✗ Заказ {order_number} не появился в элементах за {timeout} секунд")
            
    @allure.step("Ждем закрытие модального окна")
    def waiting_close_modal_window(self):
        self.is_element_not_visible(MainPageLocators.MODAL_WINDOW, timeout=10)
    
    
    