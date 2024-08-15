from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class MainPage(BasePage):
    CAROUSEL_BANNER = By.CSS_SELECTOR, "#carousel-banner-1"
    FIRST_PRODUCT = By.XPATH, '//div[@id="content"]/div[2]/div[2]/div/div[2]/form/div/button'
    PRICE_OF_ANY_PRODUCT_MAIN = By.CSS_SELECTOR, "span.price-new"

    def get_carousel(self):
        """Получение карусели Featured"""
        self.logger.debug("Get carousel")
        return self.get_element(self.CAROUSEL_BANNER)

    def add_to_cart_first_product_of_featured(self):
        """Добавление в корзину первого товара из Featured"""
        self.logger.info("Add to Cart product in Featured")
        self.click(self.FIRST_PRODUCT)

    def get_price_of_any_product_main(self):
        """Получение стоимости одного из продуктов на главной странице"""
        self.logger.info("Get price of product")
        return self.get_element(self.PRICE_OF_ANY_PRODUCT_MAIN)

