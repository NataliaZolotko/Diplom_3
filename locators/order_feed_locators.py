from selenium.webdriver.common.by import By


class OrderFeedLocators:
    PAGE_TITLE = (By.XPATH, "//div[@class='OrderFeed_orderFeed__2RO_j']")
        
    TODAY_ORDERS_COUNT = (By.XPATH, "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::*[contains(@class, 'digits-large') or contains(@class, 'OrderFeed_number')]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::*[contains(@class, 'digits-large') or contains(@class, 'OrderFeed_number')]")
    #NUMBER_ORDER_AT_WORK = (By.XPATH, "//p[contains(text(), 'В работе:')]/following-sibling::ul[1]//li")
    #NUMBER_ORDER_AT_WORK = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[1]//li")
    NUMBER_ORDER_AT_WORK = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    NUMBER_ORDER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")