import random
import string
import time
import keyboard
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AccessListPage(BasePage):
    ADD_BUTTON = By.XPATH, '//*[@class="btn btn-primary mr-3 btn-icon"]'
    PHONE_FIELD = By.XPATH, '//*[@class="custom-input vue-driven"]'
    STATUS_DD = By.XPATH, '//*[@class="custom-select-input"]'
    STATUS_ACTIVED = By.XPATH, '//*[@data-id="ACTIVATED"]'
    STATUS_DEACTIVED = By.XPATH, '//*[@data-id="DEACTIVATED"]'
    TARGETING_DD = By.XPATH, '//*[@class="custom-select-input multiple all-selected"]'
    TARGETING_DD_OPEN = By.XPATH, '//*[@class="custom-select-input dropdown-opened multiple"]'
    TARGETING_DD_SELECTED = By.XPATH, '//*[@class="custom-select-input multiple"]'
    COMMENT_FIELD = By.XPATH, '//*[@class="custom-textarea"]'
    SAVE_BUTTON = By.XPATH, '//*[@class="btn btn-primary ml-2"]'
    FIRST_PHONE = By.XPATH, '//*[@data-row_number="0"]'
    DATA_BLOCK_PHONE = By.XPATH, '//*[text()="Номер телефона"]'
    DATA_BLOCK_STATUS = By.XPATH, '//*[text()="Статус"]'
    DATA_BLOCK_COMMENT = By.XPATH, '//*[text()="Комментарий"]'
    DATA_BLOCK_DATE_CREATE = By.XPATH, '//*[text()="Дата создания"]'
    DATA_BLOCK_EDIT_BUTTON = By.XPATH, '//a[contains(text(),"Редактировать")]'
    HOTSPOT_BLOCK_NAME = By.XPATH, '//*[text()="Сети Wi-Fi"]'
    HOTSPOT_BLOCK_SERVICE = By.XPATH, '//*[text()="Услуга"]'
    HOTSPOT_BLOCK_SSID = By.XPATH, '//*[text()="SSID"]'
    HOTSPOT_BLOCK_TYPE = By.XPATH, '//*[text()="Тип"]'
    HOTSPOT_BLOCK_REGION = By.XPATH, '//*[text()="Регион"]'
    HOTSPOT_BLOCK_ADDRESS = By.XPATH, '//*[text()="Адрес"]'
    HOTSPOT_BLOCK_STATUS = By.XPATH, '//*[text()="Статус"]'
    PAGINATION = By.XPATH, '//*[@class="pagination list-group-horizontal"]'
    ICON_RIGHT = By.XPATH, '//*[@href="#icon-right"]'
    ICON_LEFT = By.XPATH, '//*[@href="#icon-left"]'
    PAGE_NUM_AFT_1 = By.XPATH, '//*[@class="list-group-item px-3 py-2"]'
    SEARCH_FIELD = By.XPATH, '//*[@name="AccessListSearch[searchstring]"]'
    SEARCH_FIELD_RESET = By.XPATH, '//*[@data-action="reset"]'
    SEARCH_TITLE = By.XPATH, '//*[@class="text-center"]'
    DELETE_BUTTON_FOR_HS = By.XPATH, '//*[@href="#icon-close"]'
    CANCEL_BUTTON = By.XPATH, '//*[@class="btn btn-primary-ghost"]'


    def click_on_add_new_acc_list_button(self):
        """Нажатие кнопки +Добавить"""
        self.logger.info("Click add new poll button")
        self.click(self.ADD_BUTTON)

    def generate_phone_number(self):
        """Генерация номера"""
        self.logger.info("Generate phone")
        area_code = random.randint(900, 999)
        first_three_digits = random.randint(900, 999)
        second_two_digits = random.randint(10, 99)
        third_two_digits = random.randint(10, 99)
        phone_number = f"({area_code}){first_three_digits}-{second_two_digits}-{third_two_digits}"
        return phone_number

    def input_phone_number(self, phone):
        """Заполнение номера"""
        self.logger.info("Input phone")
        self.input_value(self.PHONE_FIELD, phone)
        return phone

    def select_active_status(self):
        """Выбор активного статуса"""
        self.logger.info("Select active status")
        self.click(self.STATUS_DD)
        self.click(self.STATUS_ACTIVED)

    def select_inactive_status(self):
        """Выбор неактивного статуса"""
        self.logger.info("Select inactive status")
        self.click(self.STATUS_DD)
        self.click(self.STATUS_DEACTIVED)

    def select_hotspots_by_ids(self, ssid_ids: list):
        """Выбор сетей по ID если указаны"""
        self.logger.info("Select hotspots by ID, if dict not empty")
        if ssid_ids:
            self.click(self.TARGETING_DD)
            for i in ssid_ids:
                SSID_PATH = By.XPATH, f'//*[@data-id="{i}"]'
                self.click(SSID_PATH)
            self.click(self.TARGETING_DD_OPEN)
        else:
            pass

    def input_comment(self, comment):
        """Ввод комментария"""
        self.logger.info("Input comment")
        if comment:
            self.input_value(self.COMMENT_FIELD, comment)
        else:
            pass

    def save_phone(self):
        """Добавление номера"""
        self.logger.info("Save phone")
        self.click(self.SAVE_BUTTON)

    def cancel_saving_phone(self):
        """Отмена добавления номера"""
        self.logger.info("Cancel saving phone")
        self.click(self.CANCEL_BUTTON)

    def check_phone_on_main_acc_list_page(self, phone):
        """Проверка наличия телефона в списке"""
        self.logger.info("Check phone after add")
        phone_in_correct_format = phone.replace('(', '+7(')
        SEARCH = By.XPATH, f'//*[text()="{phone_in_correct_format}"]'
        self.get_element(SEARCH)
        return phone

    def check_phone_with_7(self, phone):
        """Проверка наличия телефона в списке"""
        self.logger.info("Check phone after add")
        phone_in_correct_format = phone.replace('(', ' (').replace(')', ') ')
        SEARCH = By.XPATH, f'//*[text()="{phone_in_correct_format}"]'
        self.get_element(SEARCH)
        return phone

    def check_phone_without_7(self, phone):
        """Проверка наличия телефона в списке"""
        self.logger.info("Check phone after add")
        phone_format = phone.replace('(', ' (').replace(')', ') ')
        phone_in_correct_format = '+7' + phone_format
        SEARCH = By.XPATH, f'//*[text()="{phone_in_correct_format}"]'
        self.get_element(SEARCH)
        phone_corr = '+7' + phone
        return phone_corr

    def check_hotspots(self, hs_q_old, hs_q_new):
        """Проверка количества хотспотов в таблице"""
        self.logger.info("Check hotspots")
        new_value = hs_q_old - 1
        if new_value == hs_q_new:
            pass
        else:
            raise ValueError("Error: Hotspots list not changed")

    def check_comments(self, comment_old, comment_new):
        """Проверка количества хотспотов в таблице"""
        self.logger.info("Check hotspots")
        if comment_old == comment_new:
            raise ValueError("Error: Comment not changed")
        else:
            pass

    def open_first_phone(self):
        """Редактирование первого телефона"""
        self.logger.info("Edit first phone")
        self.click(self.FIRST_PHONE)

    def check_hotspots_on_phone_page(self, ssid_ids: list):
        """Проверка сетей на странице телефона по ID если указаны"""
        self.logger.info("Check hotspots on phone page by ID, if dict not empty")
        if ssid_ids:
            for i in ssid_ids:
                SSID_PATH = By.XPATH, f'//*[@data-id="{i}"]'
                self.get_element(SSID_PATH)
        else:
            pass

    def check_data_block_in_lk(self):
        """Проверка основного блока данных о телефоне"""
        self.logger.debug("Gheck data block in lk")
        self.get_element(self.DATA_BLOCK_PHONE)
        self.get_element(self.DATA_BLOCK_STATUS)
        self.get_element(self.DATA_BLOCK_COMMENT)
        self.get_element(self.DATA_BLOCK_DATE_CREATE)
        self.get_element(self.DATA_BLOCK_EDIT_BUTTON)

    def check_hotspots_block_in_lk(self):
        """Проверка блока сетей"""
        self.logger.debug("Gheck hotspots block in lk")
        self.get_element(self.HOTSPOT_BLOCK_NAME)
        self.get_element(self.HOTSPOT_BLOCK_SERVICE)
        self.get_element(self.HOTSPOT_BLOCK_SSID)
        self.get_element(self.HOTSPOT_BLOCK_TYPE)
        self.get_element(self.HOTSPOT_BLOCK_REGION)
        self.get_element(self.HOTSPOT_BLOCK_ADDRESS)

    def check_pagination(self):
        """Проверка наличия и работы пагинации"""
        self.logger.debug("Check pagination")
        try:
            pagination = self.get_elements(self.PAGINATION)
            if len(pagination) > 0:
                page_after_1 = self.get_elements(self.PAGE_NUM_AFT_1)
                num_of_page = len(page_after_1)
                if num_of_page < 10:
                    n = random.randint(2, num_of_page)
                    PAGE_PATH = By.XPATH, f'//*[@href="/network/access-point/index/?page={n}"]'
                    self.click(PAGE_PATH)
                    self.click(self.ICON_RIGHT)
                    self.click(self.ICON_LEFT)
                else:
                    n = random.randint(2, 10)
                    PAGE_PATH = By.XPATH, f'//*[@href="/network/access-point/index/?page={n}"]'
                    self.click(PAGE_PATH)
                    self.click(self.ICON_RIGHT)
                    self.click(self.ICON_LEFT)
            else:
                pass
        except TimeoutException:
            pass

    def check_phone_status_in_table_on_mian_ap_page(self):
        """Проверка значения статуса телефонного номера на принадлежность списку"""
        self.logger.debug("Check phone status in table on main ap page")
        client_phone_status = ['Активный',
                               'Неактивный'
                               ]
        for status in client_phone_status:
            locator = By.XPATH, f'//*[@title="{status}"]'
            locators = self.get_elements(locator)
            if len(locators) > 0:
                pass
            else:
                raise ValueError("Error: Status is empty")

    def check_phone_table_on_mp_in_lk(self):
        """Проверка блока сетей на главной"""
        self.logger.debug("Gheck hotspots table in lk")
        self.get_element(self.DATA_BLOCK_STATUS)
        self.get_element(self.DATA_BLOCK_PHONE)
        self.get_element(self.DATA_BLOCK_COMMENT)
        self.get_element(self.DATA_BLOCK_DATE_CREATE)

    def get_first_phone(self):
        """Получение первого номера телефона"""
        self.logger.debug("Get first phone")
        SEARCH = By.XPATH, '//*[@id="subscriber"]/table/tbody/tr[1]/td[2]'
        phone = self.get_element(SEARCH)
        phone_num = phone.text
        return phone_num

    def get_first_comment(self):
        """Получение первого комментария"""
        self.logger.debug("Get first comment")
        SEARCH = By.XPATH, '//*[@id="subscriber"]/table/tbody/tr[1]/td[3]'
        comment_row = self.get_element(SEARCH)
        comment = comment_row.text
        return comment

    def check_search_phone(self, phone):
        """Проверка поиска номера телефона с маской и без"""
        self.logger.debug("Check search phone")
        phone_row = phone[2:].replace("(", "").replace(")", "").replace("-", "")
        self.input_value(self.SEARCH_FIELD, phone_row)
        keyboard.press('enter')
        time.sleep(0.3)
        SEARCH_PHONE_PATH = By.XPATH, f'//*[text()="{phone}"]'
        elements_1 = self.get_elements(SEARCH_PHONE_PATH)
        if len(elements_1) == 1:
            self.click(self.SEARCH_FIELD_RESET)
        else:
            raise ValueError("Error: Phone not found")
        self.input_value(self.SEARCH_FIELD, phone)
        keyboard.press('enter')
        time.sleep(0.3)
        elements_2 = self.get_elements(SEARCH_PHONE_PATH)
        if len(elements_2) == 1:
            self.click(self.SEARCH_FIELD_RESET)
        else:
            raise ValueError("Error: Phone not found")

    def check_search_by_comment(self, comment):
        """Проверка поиска по комментарию"""
        self.logger.debug("Check search by comment")
        half_length = len(comment) // 2
        search_value = comment[:half_length]
        self.input_value(self.SEARCH_FIELD, search_value)
        keyboard.press('enter')
        time.sleep(0.3)
        SEARCH_COMMENT_PATH = By.XPATH, f'//*[text()="{comment}"]'
        elements_1 = self.get_elements(SEARCH_COMMENT_PATH)
        if len(elements_1) >= 1:
            self.click(self.SEARCH_FIELD_RESET)
        else:
            raise ValueError("Error: Comment not found")

    def check_search_by_non_existent_value(self):
        """Проверка поиска по комментарию"""
        self.logger.debug("Check search by comment")
        characters = string.ascii_letters + string.digits + string.punctuation
        search_value = ''.join(random.choice(characters) for i in range(20))
        self.input_value(self.SEARCH_FIELD, search_value)
        keyboard.press('enter')
        time.sleep(0.3)
        elements = self.get_elements(self.SEARCH_TITLE)
        if len(elements) == 1:
            self.click(self.SEARCH_FIELD_RESET)
        else:
            raise ValueError("Error: Value exist and found")

    def edit_phone(self):
        """Отркытие формы редактирования телефона"""
        self.logger.debug("Edit phone")
        self.click(self.DATA_BLOCK_EDIT_BUTTON)

    def check_field_on_edit_page(self):
        """Проверка полей"""
        self.logger.debug("Check field on phone edit page")
        self.get_element(self.PHONE_FIELD)
        self.get_element(self.STATUS_DD)
        self.get_element(self.TARGETING_DD_SELECTED)
        self.get_element(self.COMMENT_FIELD)

    def input_random_comment(self):
        """Ввод рандомного значения в комментарий"""
        self.logger.debug("Input random comment")
        characters = string.ascii_letters + string.digits + string.punctuation
        base_value = 'Autotest random value: '
        comment_value = ''.join(random.choice(characters) for i in range(20))
        value = base_value + comment_value
        self.input_value(self.COMMENT_FIELD, value)
        return value

    def del_last_hotspot_in_dd(self):
        """Удаление последнего хотспота из списка выбранных"""
        self.logger.debug("Delete last hotspot in dropdown")
        del_buttons = self.get_elements(self.DELETE_BUTTON_FOR_HS)
        del_but = del_buttons.pop()
        del_but.click()

    def get_hs_quantity(self):
        """Получение количества хотспотов (при <20)"""
        self.logger.debug("Get hs qantity")
        titles = self.get_elements(self.SEARCH_TITLE)
        hotspots = len(titles) - 1
        return hotspots


