from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def get_element(self, locator: tuple, timeout=5):
        """Получение конкретного элемента по локатору"""
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=5):
        """Получение нескольких элементов по локатору"""
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: tuple):
        """Нажатие на кнопку по локатору"""
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        """Ввод данных в поле"""
        self.click(locator)
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def get_alert(self, timeout=3):
        """Получение алерта на странице"""
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())

    def back_page(self):
        """Назад"""
        self.browser.back()
