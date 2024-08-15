from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PATH = "/identity/user/login/"
    EMAIL_FIELD = By.XPATH, '//a[@id="customerlogin-email"]'
    PASSWORD_FIELD = By.XPATH, '//*[@id="customerlogin-password"]'
    ENTER_BUTTON = By.XPATH, '//*[@class="btn btn-primary"]'
    REMEMBER = By.XPATH, '//*[@id="customerlogin-remember"]'
    RECOVER = By.XPATH, '//*[@class="btn btn-primary-ghost"]'

    def open(self):
        """Открытие страницы"""
        self.logger.info("Open login page")
        url = self.browser.current_url
        self.browser.get(url + self.LOGIN_PATH)

    def login(self, username, password):
        """Авторизация в ЛК/ПА"""
        self.logger.info("Log In process")
        self.input_value(self.EMAIL_FIELD, username)
        self.input_value(self.PASSWORD_FIELD, password)
        self.click(self.ENTER_BUTTON)
        return self
