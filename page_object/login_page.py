from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class LoginPage(BasePage):
    PATH = "identity/user/login/"
    EMAIL_FIELD = By.CSS_SELECTOR, "#customerlogin-email"
    PASSWORD_FIELD = By.CSS_SELECTOR, "#customerlogin-password"
    ENTER_BUTTON = By.XPATH, '//*[@name="login-button"]'
    REMEMBER = By.XPATH, '//*[@id="customerlogin-remember"]'
    RECOVER = By.XPATH, '//*[@class="btn btn-primary-ghost"]'
    SSO_USERNAME_FIELD = By.CSS_SELECTOR, "#username"
    SSO_PASSWORD_FIELD = By.CSS_SELECTOR, "#password"
    SSO_ENTER_BUTTON = By.CSS_SELECTOR, "#kc-login"
    SSO_REMEMBER = By.XPATH, '//*[@class="rt-checkbox__label"]'
    SSO_RECOVER = By.CSS_SELECTOR, "#forgot_password"
    SSO_SKIP_CHECK_PHONE = By.CSS_SELECTOR, "#update-profile-skip"

    def local_login(self, stand, username, password):
        """Авторизация в ЛК локально"""
        self.logger.info("Log In process")
        stands = ['test', 'pre']
        if stand in stands:
            LOCAL_URL = f"https://client.{stand}.wf.rt.ru/identity/user/login/"
            self.browser.get(LOCAL_URL)
            self.input_value(self.EMAIL_FIELD, username)
            self.input_value(self.PASSWORD_FIELD, password)
            self.click(self.ENTER_BUTTON)
            return self
        else:
            self.input_value(self.EMAIL_FIELD, username)
            self.input_value(self.PASSWORD_FIELD, password)
            self.click(self.ENTER_BUTTON)
            return self

    def sso_login(self, username, password):
        """Авторизация в ЛК через SSO"""
        self.logger.info("Log In SSO")
        self.input_value(self.SSO_USERNAME_FIELD, username)
        self.input_value(self.SSO_PASSWORD_FIELD, password)
        self.click(self.SSO_ENTER_BUTTON)
        self.click(self.SSO_SKIP_CHECK_PHONE)
        return self
