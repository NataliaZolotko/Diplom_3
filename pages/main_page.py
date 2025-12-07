from pages.base_page import BasePage
from locators.basic_function_locators import MainPageLocators
from data import *
import allure
import time


class MainPage(BasePage):
    @allure.step('Открываем страницу "Главная"')
    def open_main_page(self):
        self.open(main_site)
        time.sleep(3)
           
    @allure.step("Кликнуть на Конструктор")
    def click_constructor(self):
        time.sleep(3)
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на Ленту заказов")
    def click_order_feed(self):
        time.sleep(2)
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Кликнуть на ингредиент из любого раздела")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)
        
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):    
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.CONSTRUCTOR_AREA)
    
    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        try:
            counter_element = self.find_element(MainPageLocators.INGREDIENT_COUNTER, timeout=3)
            counter_text = counter_element.text
            if counter_text and counter_text.isdigit():
                return int(counter_text)
            else:
                return 1
        except:
            return 0
    
    @allure.step("Проверить, что открыт конструктор")
    def is_constructor_opened(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_AREA)
    
    @allure.step("Перейти в Личный кабинет")
    def go_to_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_open(self):
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
    
    @allure.step("Авторизация")
    def authorization(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
        time.sleep(2)
        email_input = self.find_element(MainPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(Auth.email)
        password_input = self.find_element(MainPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(Auth.password)
        self.click(MainPageLocators.ENTER_BUTTON)
        time.sleep(3)
        return True
       
       
       