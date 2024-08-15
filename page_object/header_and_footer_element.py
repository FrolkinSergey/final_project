from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class HeaderElement(BasePage):
    BRAND = By.XPATH, '//*[@class="navbar-brand"]'
    PROFILE = By.XPATH, '//*[@href="icon-profile"]'
    LOGOUT_BUTTON = By.XPATH, '//*[@href="icon-sign-out"]'

    CART_HIDDEN = By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle"]'
    CART_SHOW = By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle show"]'
    EMPTY_CART_TEXT = By.XPATH, '//*[@class="text-center p-4"]'
    DESKTOPS = By.XPATH, '//*[@class="nav-link dropdown-toggle"]'
    SHOW_ALL = By.XPATH, '//*[@class="see-all"]'
    PRODUCT_CARD_IN_CART = By.XPATH, '//*[@class="table table-striped mb-2"]'
    CARD_TABLE_IN_CART = By.XPATH, '//*[@class="table table-sm table-bordered mb-2"]'
    DELETE_BUTTON_IN_CART = By.XPATH, '//*[@class="btn btn-danger"]'
    CURRENCY_DROPDOWN = By.XPATH, '//*[@class="dropdown-toggle"]'
    CURRENCY_EURO = By.XPATH, '//*[@href="EUR"]'
    CURRENCY_POUND_STERLING = By.XPATH, '//*[@href="GBP"]'
    CURRENCY_US_DOLLAR = By.XPATH, '//*[@href="USD"]'

    def get_navbar_brand(self):
        """Полчуение поля бренда - достоверность нахождения в зоне Wi-Fi 2.0 ЛК/ПА"""
        self.logger.debug("Get navbar_brand")
        return self.get_element(self.BRAND)

    def get_(self):
        """Полчуение поля бренда - достоверность нахождения в зоне Wi-Fi 2.0 ЛК/ПА"""
        self.logger.debug("Get navbar_brand")
        return self.get_element(self.BRAND)

    def click_logout_button(self):
        """Нажатие кнопки выхода ЛК/ПА"""
        self.logger.debug("Get logout button")
        self.click(self.LOGOUT_BUTTON)

    def click_profile_button(self):
        """Нажатие кнопки профиля ЛК/ПА"""
        self.logger.debug("Get search field")
        self.click(self.PROFILE)







    def click_cart_hidden(self):
        """Нажание на пустую корзину"""
        self.logger.info("Click on empty cart")
        self.click(self.CART_HIDDEN)

    def click_cart_show(self):
        """Нажатие на корзину с товаром"""
        self.logger.info("Click on cart with products")
        self.click(self.CART_SHOW)

    def check_empty_cart(self):
        """Проверка пустоты корзины"""
        self.logger.info("Check empty cart")
        return self.get_element(self.EMPTY_CART_TEXT)

    def click_any_dropdown(self):
        """Нажатие одного из полей в меню"""
        self.logger.info("Click on any dropdown")
        self.click(self.DESKTOPS)

    def click_show_all(self):
        """Нажтие на строку Show All"""
        self.logger.info("Click on show all")
        self.click(self.SHOW_ALL)

    def get_elements_in_cart_with_added_product(self):
        """Получение элементов в корзине с любым продуктом"""
        self.logger.debug("Get elements in cart with product")
        self.get_element(self.PRODUCT_CARD_IN_CART)
        self.get_element(self.CARD_TABLE_IN_CART)
        self.get_element(self.DELETE_BUTTON_IN_CART)
        return self

    def click_change_euro(self):
        """Выбор валюты - Евро"""
        self.logger.info("Change Euro")
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.CURRENCY_EURO)
        return self

    def click_change_pound(self):
        """Выбор валюты - Пунд"""
        self.logger.info("Change Pound")
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.CURRENCY_POUND_STERLING)
        return self

    def click_change_dollar(self):
        """Выбор валюты - Доллар"""
        self.logger.info("Change Dollar")
        self.click(self.CURRENCY_DROPDOWN)
        self.click(self.CURRENCY_US_DOLLAR)
        return self


class FooterElement(BasePage):
    FOOTER = By.XPATH, '//*[@class ="container"]'

    def get_footer(self):
        self.logger.debug("Get footer")
        """Получение футера на базовой странице"""
        return self.get_element(self.FOOTER)
