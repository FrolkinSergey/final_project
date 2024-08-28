from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class HeaderElement(BasePage):
    PROFILE = By.XPATH, '//*[@href="#icon-profile"]'
    LOGOUT_BUTTON = By.XPATH, '//*[@href="#icon-sign-out"]'
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

    def click_logout_button(self):
        """Нажатие кнопки выхода ЛК/ПА"""
        self.logger.debug("Get logout button")
        self.click(self.LOGOUT_BUTTON)

    def click_profile_button(self):
        """Нажатие кнопки профиля ЛК/ПА"""
        self.logger.debug("Get search field")
        self.click(self.PROFILE)

class FooterElement(BasePage):
    FOOTER = By.XPATH, '//*[@class ="container"]'

    def get_footer(self):
        self.logger.debug("Get footer")
        """Получение футера на базовой странице"""
        return self.get_element(self.FOOTER)
