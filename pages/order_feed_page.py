from pages.base_page import BasePage
from locators.basic_function_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class OrderFeedPage(BasePage):
    @allure.step("Проверить, что открыта лента заказов")
    def is_order_feed_opened(self):
        return self.is_element_visible(OrderFeedLocators.PAGE_TITLE)
       
    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        try:
            element = self.driver.find_element(*OrderFeedLocators.TODAY_ORDERS_COUNT)
            text = element.text.strip()
            import re
            match = re.search(r'\d+', text)
            if match:
                return int(match.group())
            else:
                return 0       
        except Exception as e:
            print(f"Ошибка: {e}")
            return None   
        
    @allure.step("Получить количество выполненных заказов за все время")
    def get_total_orders_count(self):
        try:
            element = self.driver.find_element(*OrderFeedLocators.TOTAL_ORDERS_COUNT)
            text = element.text.strip()
            import re
            match = re.search(r'\d+', text)
            if match:
                return int(match.group())
            else:
                return 0       
        except Exception as e:
            print(f"Ошибка: {e}")
            return None            
            
    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        try:
            elements = self.find_elements(OrderFeedLocators.NUMBER_ORDER_AT_WORK)
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
        time.sleep(5)
    
    @allure.step("Оформляем заказ с получением номера")
    def place_an_order_and_get_number(self):
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        order_button.click()
        order_modal = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_WINDOW))
        time.sleep(20)
        order_number_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderFeedLocators.NUMBER_ORDER))
        order_number_text = order_number_element.text
        print(f"Текст номера заказа: {order_number_text}")
        import re
        match = re.search(r'\d+', order_number_text)
        if match:
            order_number = match.group()
            print(f"Извлеченный номер заказа: {order_number}")
        else:
            order_number = order_number_text
            print(f"Используем полный текст как номер: {order_number}")
        
        return order_number
    
    @allure.step("Оформляем заказ с получением номера без ожидания длительной загрузки")
    def place_an_order_and_get_number_without_waiting(self):
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        order_button.click()
        order_modal = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_WINDOW))
        time.sleep(5)
        order_number_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderFeedLocators.NUMBER_ORDER))
        order_number_text = order_number_element.text
        print(f"Текст номера заказа: {order_number_text}")
        import re
        match = re.search(r'\d+', order_number_text)
        if match:
            order_number = match.group()
            print(f"Извлеченный номер заказа: {order_number}")
        else:
            order_number = order_number_text
            print(f"Используем полный текст как номер: {order_number}")
        
        return order_number