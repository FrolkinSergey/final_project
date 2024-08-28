from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class ModalSurveyPage(BasePage):
    CLOSE_MODAL_WIN = By.XPATH, '//*[@class="modal-action close"]'

    def close_modal_win(self):
        """Закрытие модального окна опроса(если есть)"""
        self.logger.debug("Close survey modal window")
        try:
            self.click(self.CLOSE_MODAL_WIN)
        except TimeoutException:
            pass
