from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class MainPage(BasePage):
    EQUIP_MENU = By.XPATH, '//*[@href="#icon-nav-ap"]'
    AP_SUBMENU = By.XPATH, '//*[text()="Точки доступа"]'
    POOL_MENU = By.XPATH, '//*[@href="/promo/poll/"]'
    ACC_LIST_MENU = By.XPATH, '//*[@href="/network/access-list/"]'

    def go_back(self):
        self.back_page()

    def get_url(self):
        """Получение url"""
        self.logger.debug("Get url")
        url = self.browser.current_url
        return url

    def get_path(self, url):
        """Получение PATH"""
        self.logger.info("Get poll path")
        full_url = self.browser.current_url
        path_row = str(full_url.replace(url, "/"))
        path = path_row[:(-1)]
        return path

    def open_access_points_page(self):
        """Открытие главной страницы Точки доступа"""
        self.logger.debug("Get carousel")
        self.click(self.EQUIP_MENU)
        self.click(self.AP_SUBMENU)

    def open_poll_page(self):
        """Открытие главной страницы Опросы"""
        self.logger.debug("Get carousel")
        self.click(self.POOL_MENU)

    def open_access_list_page(self):
        """Открытие главной страницы Доступ по списку"""
        self.logger.debug("Get carousel")
        self.click(self.ACC_LIST_MENU)
