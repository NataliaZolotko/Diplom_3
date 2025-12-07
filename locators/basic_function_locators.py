from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    INGREDIENT = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']")
    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")   
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button [@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    
    INGREDIENT_COUNTER = (By.XPATH, "(//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'])[1]//p[@class='counter_counter__num__3nue1']")
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[@class= 'BurgerConstructor_basket__list__l9dp_']")
   
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")