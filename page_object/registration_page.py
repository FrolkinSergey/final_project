from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class RegistrationPage(BasePage):
    PATH = "/index.php?route=account/register"
    REG_TITLE = By.XPATH, '//*[text()="Register Account"]'
    FIRSTNAME_FIELD = By.CSS_SELECTOR, "#input-firstname"
    LASTNAME_FIELD = By.CSS_SELECTOR, '[name="lastname"]'
    EMAIL_FIELD = By.CSS_SELECTOR, "#input-email"
    PASSWORD_FIELD = By.CSS_SELECTOR, "#input-password"
    NEWSLETTER_CHECKBOX = By.CSS_SELECTOR, "#input-newsletter"
    AGREE_CHECKBOX = By.CSS_SELECTOR, '[name="agree"]'
    CONTINUE_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    COMPLETED_TEXT = By.XPATH, '//*[text()="Your Account Has Been Created!"]'

    def open(self):
        """Открытие"""
        self.logger.info("Open registration page")
        url = self.browser.current_url
        self.browser.get(url + self.PATH)

    def get_reg_title(self):
        """Получение названия страницы регистрации"""
        self.logger.debug("Get title on registration page")
        return self.get_element(self.REG_TITLE)

    def get_firstname_input_field(self):
        """Получение поля FirstName"""
        self.logger.debug("Get input field for FirstName")
        return self.get_element(self.FIRSTNAME_FIELD)

    def get_lastname_input_field(self):
        """Получение поляLastName"""
        self.logger.debug("Get input field for LastName")
        return self.get_element(self.LASTNAME_FIELD)

    def get_email_input_field(self):
        """Получение поля Email"""
        self.logger.debug("Get input field for Email")
        return self.get_element(self.EMAIL_FIELD)

    def get_password_input_field(self):
        """Получение поля Password"""
        self.logger.debug("Get input field for Password")
        return self.get_element(self.PASSWORD_FIELD)

    def get_newsletter_checkbox(self):
        """Получение чек-бокса новостной рассылки на почту"""
        self.logger.debug("Get newsletter checkbox")
        return self.get_element(self.NEWSLETTER_CHECKBOX)

    def get_agree_checkbox(self):
        """Получение чек-бокса принятия пользовательского соглашения"""
        self.logger.debug("Get agree checkbox")
        return self.get_element(self.AGREE_CHECKBOX)

    def get_continue_button(self):
        """Получение кнопки Continue"""
        self.logger.debug("Get continue button")
        return self.get_element(self.CONTINUE_BUTTON)

    def register_page_input_value(self, first_name, last_name, email, password):
        """Ввод данных в обязательные пола на странице регистарции"""
        self.logger.info("Input requirement field")
        self.input_value(self.FIRSTNAME_FIELD, first_name)
        self.input_value(self.LASTNAME_FIELD, last_name)
        self.input_value(self.EMAIL_FIELD, email)
        self.input_value(self.PASSWORD_FIELD, password)
        return self

    def enter_checkboxes(self):
        """Проставление чек-боксов"""
        self.logger.info("Enter checkboxes")
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.AGREE_CHECKBOX)
        return self

    def click_continue(self):
        """Нажание на кнопку Continue"""
        self.logger.info("Click Continue button")
        self.click(self.CONTINUE_BUTTON)

    def check_registration(self):
        """Проверка регистрации по тексту подтверждения"""
        self.logger.info("Check registration")
        return self.get_element(self.COMPLETED_TEXT)
