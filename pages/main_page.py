from pages.base_page import BasePage
from locators.basic_function_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data import *
import allure



class MainPage(BasePage):
    @allure.step('Открываем страницу "Главная"')
    def open_main_page(self):
        self.open(main_site)
        self.wait_for_page_loaded()
           
    @allure.step("Кликнуть на Конструктор")
    def click_constructor(self):
        constructor_button = WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
    )
        constructor_button.click()
    
    @allure.step("Кликнуть на Ленту заказов")
    def click_order_feed(self):
        self.wait_for_page_loaded()
        order_feed_button = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
    )
        order_feed_button.click()
    
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
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_AREA,timeout=5)
    
    @allure.step("Перейти в Личный кабинет")
    def go_to_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_open(self):
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW, timeout=5)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON, timeout=20)
    
    
    @allure.step("Авторизация")
    def authorization(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
        email_input = self.find_element(MainPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(Auth.email)
        password_input = self.find_element(MainPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(Auth.password)
        self.click(MainPageLocators.ENTER_BUTTON)
        return True
       
       
    @allure.step("Дождаться загрузки конструктора")
    def wait_for_constructor_loaded(self, timeout=15):
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_AREA, timeout)
    
    @allure.step("Дождаться добавления ингредиента")
    def wait_for_ingredient_added(self, timeout=10):
        self.wait_for_visible(MainPageLocators.INGREDIENT_COUNTER, timeout)