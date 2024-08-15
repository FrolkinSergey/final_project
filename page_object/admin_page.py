from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/administration"
    LOG_TITLE = By.XPATH, '//*[text()=" Please enter your login details."]'
    USERNAME_INPUT_FIELD = By.CSS_SELECTOR, "#input-username"
    PASSWORD_INPUT_FIELD = By.CSS_SELECTOR, "#input-password"
    SUBMIT_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
    LOGIN_PAGE_FOOTER = By.XPATH, '//*[text()=" © 2009-2024 All Rights Reserved."]'
    LOGOUT_BUTTON = By.CSS_SELECTOR, "#nav-logout"
    CATALOG = By.XPATH, '//*[text()=" Catalog"]'
    CATALOG_OPEN = By.XPATH, '//*[@class="collapse show"]'
    PRODUCTS_IN_CATALOG = By.XPATH, '//*[text()="Products"]'
    ADD_NEW_PRODUCT_BUTTON = By.XPATH, '//*[@class="btn btn-primary"]'
    ADDPAGE_PRODUCT_NAME = By.CSS_SELECTOR, "#input-name-1"
    ADDPAGE_META_TAG_TITLE = By.CSS_SELECTOR,  "#input-meta-title-1"
    ADDPAGE_TAB_DATA = By.XPATH, '//*[@href="#tab-data"]'
    ADDPAGE_MODEL = By.CSS_SELECTOR, '[name="model"]'
    ADDPAGE_TAB_SEO = By.XPATH, '//*[@href="#tab-seo"]'
    ADDPAGE_SEO_DEFAULT = By.CSS_SELECTOR, '[name="product_seo_url[0][1]"]'
    ADDPAGE_SAVE_BUTTON = By.XPATH, '//*[@class="fa-solid fa-floppy-disk"]'
    CHOICE_CHECKBOX = By.CSS_SELECTOR, '[name="selected[]"]'
    DELETE_BUTTON = By.XPATH, '//*[@class="btn btn-danger"]'


    def open(self):
        """Открытие страницы"""
        self.logger.info("Open admin page")
        url = self.browser.current_url
        self.browser.get(url + self.PATH)

    def get_log_title(self):
        """Получение заголовка"""
        self.logger.debug("Get login title")
        return self.get_element(self.LOG_TITLE)

    def get_username_input_field(self):
        """Получение поля вставки username"""
        self.logger.debug("Get username input field")
        return self.get_element(self.USERNAME_INPUT_FIELD)

    def get_password_input_field(self):
        """Получение поля вставки password"""
        self.logger.debug("Get password input field")
        return self.get_element(self.PASSWORD_INPUT_FIELD)

    def get_submit_button(self):
        """Получение кнопки подтверждения"""
        self.logger.debug("Get submit button")
        return self.get_element(self.SUBMIT_BUTTON)

    def get_ap_footer(self):
        """Получение футера страницы входа в админку"""
        self.logger.debug("Get admin-page footer")
        return self.get_element(self.LOGIN_PAGE_FOOTER)

    def login(self, username, password):
        """Авторизация в админке"""
        self.logger.info("Log In")
        self.input_value(self.USERNAME_INPUT_FIELD, username)
        self.input_value(self.PASSWORD_INPUT_FIELD, password)
        self.click(self.SUBMIT_BUTTON)
        return self

    def get_logout_button(self):
        """Получение кнопки выхода из админки"""
        self.logger.debug("Get logout button")
        return self.get_element(self.LOGOUT_BUTTON)

    def logout(self):
        """Выход из админки"""
        self.logger.info("Log Out")
        self.get_element(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_BUTTON)
        return self

    def open_products(self):
        """Открытие раздела Products"""
        self.logger.info("Open product")
        self.click(self.CATALOG)
        self.get_element(self.CATALOG_OPEN)
        self.click(self.PRODUCTS_IN_CATALOG)

    def click_add_new_product(self):
        self.logger.info("Click Add new product")
        """Нажатие кнопки добавления нового продукта"""
        self.click(self.ADD_NEW_PRODUCT_BUTTON)

    def input_required_field(self, product_name, meta_title, model, default):
        """Заполнение обязательных полей на странице добавления нового продукта"""
        self.logger.info("Input required field")
        self.input_value(self.ADDPAGE_PRODUCT_NAME, product_name)
        self.click(self.ADDPAGE_META_TAG_TITLE)
        self.input_value(self.ADDPAGE_META_TAG_TITLE, meta_title)
        self.click(self.ADDPAGE_TAB_DATA)
        self.input_value(self.ADDPAGE_MODEL, model)
        self.click(self.ADDPAGE_TAB_SEO)
        self.input_value(self.ADDPAGE_SEO_DEFAULT, default)
        self.click(self.ADDPAGE_SAVE_BUTTON)
        return self

    def choice_checkbox_1(self):
        """Выбор продукта из списка"""
        self.logger.info("Choice checkbox")
        self.click(self.CHOICE_CHECKBOX)

    def click_delete(self):
        """Нажатие кнопки корзины"""
        self.logger.info("Click delete")
        self.click(self.DELETE_BUTTON)

    def accept_alert(self):
        """Подтверждение в окне алерта"""
        self.logger.info("Accept Alert")
        alert = self.get_alert()
        alert.accept()

