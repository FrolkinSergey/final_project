from urllib.parse import urlparse, urlunparse
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage

AD_user = "admin_test@adm.ru"
AD_password = "q1w2e3r4"


class AdminPage(BasePage):
    EMAIL_FIELD = By.CSS_SELECTOR, "#login-email"
    PASSWORD_FIELD = By.CSS_SELECTOR, "#login-password"
    ENTER_BUTTON = By.XPATH, '//*[@name="login-button"]'
    REMEMBER = By.XPATH, '//*[@id="customerlogin-remember"]'
    RECOVER = By.XPATH, '//*[@class="btn btn-primary-ghost"]'
    AUDIT_IN_MENU = By.XPATH, '//*[@href="#icon-nav-audit"]'
    DROPDOWN_FIELD = By.XPATH, '//*[@class="custom-select-input"]'
    DROPDOWN = By.XPATH, '//*[@id="audit-search-form"]/div/div/div/fieldset/div/div[1]/div[2]/ul'
    SEARCH_BUTTON = By.CSS_SELECTOR, "#search"

    def get_adm_url(self, url):
        """Получение стенда"""
        self.logger.info("Получение стенда")
        parsed_url = urlparse(url)
        new_url = parsed_url._replace(netloc=parsed_url.netloc.replace("client", "adm"))
        adm_url = str(urlunparse(new_url))
        return adm_url

    def adm_login(self):
        """Авторизация в ПА"""
        self.logger.info("ADM Log In process")
        self.input_value(self.EMAIL_FIELD, AD_user)
        self.input_value(self.PASSWORD_FIELD, AD_password)
        self.click(self.ENTER_BUTTON)
        return self

    def adm_open_audit_and_search_by_filter(self, filter_audit):
        """Установка фильтра по объекту"""
        self.logger.info("Set filter by object")
        filter_list = [{"Все": 1}, # Название: порядковый номер !=data-key
                       {"Пользователь": 2},
                       {"Организация": 3},
                       {"Хотспот": 4},
                       {"Тема": 5},
                       {"Рекламная компания": 6},
                       {"Баннеры": 7},
                       {"Абонент": 8},
                       {"Файлы": 9},
                       {"Роль": 10},
                       {"Права": 11},
                       {"Опрос": 12},
                       {"Переводы": 13},
                       {"RT Passport": 14},
                       {"Доступ по списку": 15},
                       {"Офисная сеть": 16},
                       {"Отель": 17},
                       {"Тарифный план": 18},
                       {"Опросы пользователей": 19},
                       {"Регион": 20},
                       {"Клиент": 21}
                       ]
        for item in filter_list:
            if filter_audit in item:
                item_id = item[filter_audit]
                dd = self.get_elements(self.DROPDOWN_FIELD)
                sel_obj = dd[0]
                sel_obj.click()
                object_path = By.CSS_SELECTOR, f'.field-auditsearch-model_id li:nth-child({item_id})'
                self.click(object_path)
        self.click(self.SEARCH_BUTTON)


    def search_path_by_object(self, path):
        """Поиск по объекту"""
        self.logger.info("Search by object")
        search_path = By.XPATH, f'//*[@href="{path}"]'
        try:
            el = self.get_elements(search_path)
            if len(el) > 0:
                pass
            else:
                raise ValueError("No changes")
        except TimeoutException:
            pass

    def check_changes_in_audit(self, url, filter_audit, path):
        """Проверка изменений в Аудите"""
        self.logger.info("Check changes in Audit")
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(url)
        self.adm_login()
        self.click(self.AUDIT_IN_MENU)
        self.adm_open_audit_and_search_by_filter(filter_audit)
        self.search_path_by_object(path)
