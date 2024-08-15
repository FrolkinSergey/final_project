from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProfilePage(BasePage):
    PROFILE_TITLE = By.XPATH, '//*[text()="Профиль"]'

    def search_profile_title(self):
        """Поиск логина"""
        self.logger.debug("Search profile title")
        self.get_element(self.PROFILE_TITLE)