from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
      
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
       
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Скролл к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step("Перетащить элемент {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):    
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
    
    @allure.step("Проверить, что элемент {locator} видим")
    def is_element_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
        
    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        
    @allure.step("Проверить, что элемент {locator} не видим")
    def is_element_not_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except:
            return False
    
    
    def find_elements(self, locator, timeout=2):
        """Найти несколько элементов"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def get_element_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text.strip()
    
    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self, timeout=30):
        def page_is_loaded(driver):
            return driver.execute_script("return document.readyState") == "complete"
        WebDriverWait(self.driver, timeout).until(page_is_loaded)
    
    @allure.step("Дождаться элемента {locator}")
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    