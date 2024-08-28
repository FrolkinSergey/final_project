from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProfilePage(BasePage):
    PROFILE_TITLE = By.XPATH, '//*[text()="Профиль"]'

    def search_profile_title(self):
        """Поиск заколовка Профиль"""
        self.logger.debug("Search profile title")
        return self.get_element(self.PROFILE_TITLE)

    def get_text_by_path(self, text):
        """Нахождение конкретного текста на странице"""
        self.logger.debug("Search profile title")
        self_path = By.XPATH, f'//*[text()="{text}"]'
        return self.get_element(self_path)
