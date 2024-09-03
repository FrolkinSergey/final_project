import random
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ApPage(BasePage):
    ICONS_OF_SERVICE_ON_AP_MAIN_PAGE = By.XPATH, '//*[@style="width:1.5rem;height:1.5rem"]'
    PIC_TYPE_ON_AP_PAGE = By.XPATH, '//*[@class="text-success"]'
    FIRST_TABLE_ROW = By.XPATH, '//*[@data-row_number="0"]'
    DATA_BLOCK_NAME = By.XPATH, '//*[text()="Название"]'
    DATA_BLOCK_MAC = By.XPATH, '//*[text()="MAC"]'
    DATA_BLOCK_VENDOR = By.XPATH, '//*[text()="Производитель"]'
    DATA_BLOCK_MODEL = By.XPATH, '//*[text()="Модель"]'
    DATA_BLOCK_SN = By.XPATH, '//*[text()="Серийный номер"]'
    DATA_BLOCK_STATUS = By.XPATH, '//*[text()="Статус"]'
    DATA_BLOCK_TIS = By.XPATH, '//*[text()="Время в текущем статусе"]'
    DATA_BLOCK_DESCR = By.XPATH, '//*[text()="Описание"]'
    HOTSPOT_BLOCK = By.XPATH, '//*[@aria-labelledby="common-hotspot-tab"]'
    HSBLOCK_SERVICE = By.XPATH, '//*[text()="Услуга"]'
    HSBLOCK_SSID = By.XPATH, '//*[text()="SSID"]'
    HSBLOCK_TYPE = By.XPATH, '//*[text()="Тип"]'
    HSBLOCK_REG = By.XPATH, '//*[text()="Регион"]'
    HSBLOCK_ADDR = By.XPATH, '//*[text()="Адрес"]'
    PAGINATION = By.XPATH, '//*[@class="pagination list-group-horizontal"]'
    ICON_RIGHT = By.XPATH, '//*[@href="#icon-right"]'
    ICON_LEFT = By.XPATH, '//*[@href="#icon-left"]'
    PAGE_NUM_AFT_1 = By.XPATH, '//*[@class="list-group-item px-3 py-2"]'

    def check_ap_service_in_table_on_mian_ap_page(self):
        """Проверка значения сервиса ТД на принадлежность списку на на главной странице раздела"""
        self.logger.debug("Check ap-service in table on main ap page")
        attr_name = 'title'
        locators_list = [
            (By.XPATH, '//*[@class="text-success"]'),
            (By.XPATH, '//*[@class="text-muted"]')
        ]
        client_ap_service = ["Light Wi-Fi",
                             "Классический Wi-Fi",
                             "OTT Wi-Fi",
                             "Классический Wi-Fi, оборудование РТК",
                             "Офисная сеть"
                             ]
        for locator_by, locator_value in locators_list:
            locator = (locator_by, locator_value)
            if locator == locators_list[0]:
                loc1 = locators_list[0]
                locators1 = self.get_elements(loc1)
                for index1, element1 in enumerate(locators1):
                    iter_elements1 = locators1[index1]
                    full_title = iter_elements1.get_attribute(attr_name)
                    ap_split_value = full_title.split(":")
                    service_value_row = ap_split_value[0]
                    service_value = service_value_row.replace(', Точка доступа ', '')
                    if service_value in client_ap_service:
                        pass
                    else:
                        raise ValueError("Error: Service is not valid")
            elif locator == locators_list[1]:
                loc2 = locators_list[1]
                locators2 = self.get_elements(locator=loc2)
                for index2, element2 in enumerate(locators2):
                    iter_elements2 = locators2[index2]
                    full_title = iter_elements2.get_attribute(attr_name)
                    ap_split_value = full_title.split(":")
                    service_value_row = ap_split_value[0]
                    service_value = service_value_row.replace(', Точка доступа ', '')
                    if service_value in client_ap_service:
                        pass
                    else:
                        raise ValueError("Error: Service is not valid")
            else:
                pass

    def check_ap_status_in_table_on_main_ap_page(self):
        """Проверка значения статуса ТД на принадлежность списку на главной странице раздела"""
        self.logger.debug("Check ap-service in table on main ap page")
        attr_name = 'title'
        locators_list = [
            (By.XPATH, '//*[@class="text-success"]'),
            (By.XPATH, '//*[@class="text-muted"]')
        ]
        client_ap_status = ["Активная",
                            "Неактивная",
                            "Выключена"
                            ]
        for locator_by, locator_value in locators_list:
            locator = (locator_by, locator_value)
            if locator == locators_list[0]:
                loc1 = locators_list[0]
                locators1 = self.get_elements(loc1)
                for index1, element1 in enumerate(locators1):
                    iter_elements1 = locators1[index1]
                    full_title = iter_elements1.get_attribute(attr_name)
                    ap_split_value = full_title.split(":")
                    status_value_row = ap_split_value[1]
                    status_value = status_value_row.replace(' ', '')
                    if status_value in client_ap_status:
                        pass
                    else:
                        raise ValueError("Error: Status is not valid")
            elif locator == locators_list[1]:
                loc2 = locators_list[1]
                locators2 = self.get_elements(locator=loc2)
                for index2, element2 in enumerate(locators2):
                    iter_elements2 = locators2[index2]
                    full_title = iter_elements2.get_attribute(attr_name)
                    ap_split_value = full_title.split(":")
                    status_value_row = ap_split_value[1]
                    status_value = status_value_row.replace(' ', '')
                    if status_value in client_ap_status:
                        pass
                    else:
                        raise ValueError("Error: Status is not valid")
            else:
                pass

    def check_ap_service_in_table_on_ap_page(self):
        """Проверка значения сервиса ТД на принадлежность списку на странице точки доступа"""
        self.logger.debug("Check ap-service in table on ap page")
        client_ap_service = ['Light Wi-Fi',
                             'Light Wi-Fi\nОшибка при отправке конфигурации'
                             'Классический Wi-Fi',
                             'OTT Wi-Fi',
                             'Классический Wi-Fi, оборудование РТК',
                             'Офисная сеть'
                             ]
        for index, value in enumerate(client_ap_service):
            service = client_ap_service[index]
            if service == 'Light Wi-Fi\nОшибка при отправке конфигурации':
                PIC_SERVICE_ON_AP_PAGE = By.XPATH, f'//*[@title="{service}"]'
                try:
                    elements_row = self.get_elements(PIC_SERVICE_ON_AP_PAGE)
                    elements = len(elements_row)
                    if elements > 0:
                        break
                except TimeoutException:
                    pass
            else:
                service_valid = service + "\n"
                PIC_SERVICE_ON_AP_PAGE = By.XPATH, f'//*[@title="{service_valid}"]'
                try:
                    elements_row = self.get_elements(PIC_SERVICE_ON_AP_PAGE)
                    elements = len(elements_row)
                    if elements > 0:
                        break
                except TimeoutException:
                    pass

    def check_hs_type_in_table_on_ap_page(self):
        """Проверка значения типа сети и статуса на принадлежность спискам возможных значений"""
        self.logger.debug("Check hs-type in table on ap page")
        client_hs_type = ["Закрытая Wi-Fi сеть",
                          "Wi-Fi сеть с идентификацией"
                          ]
        client_hs_status = ["Включена",
                            "Выключена",
                            "Включена, но точка доступа недоступна"
                            ]
        attr_name = 'title'
        icons = self.get_elements(self.PIC_TYPE_ON_AP_PAGE)
        for index, element in enumerate(icons):
            iter_elements = icons[index]
            full_title_type = iter_elements.get_attribute(attr_name)
            title = full_title_type.replace(' - ', ':')
            hs_title_value = title.split(":")
            hs_type_value = hs_title_value[0]
            hs_status_value = hs_title_value[1]
            if hs_type_value in client_hs_type:
                pass
            else:
                raise ValueError("Error: Type is not valid")
            if hs_status_value in client_hs_status:
                pass
            else:
                raise ValueError("Error: Status is not valid")

    def click_on_first_table_row(self):
        """Нажатие на первую строку в таблице"""
        self.logger.debug("Click on first table row")
        self.click(self.FIRST_TABLE_ROW)

    def click_on_random_table_row(self):
        """Нажатие на рандомную строку в таблице"""
        self.logger.debug("Click on random table row")
        lines = self.get_elements(self.ICONS_OF_SERVICE_ON_AP_MAIN_PAGE)
        lines_row = len(lines)
        num_lines = lines_row - 1
        i = random.randint(0, b=num_lines)
        spec_line = lines[i]
        spec_line.click()

    def check_pagination(self):
        """Проверка наличия и работы пагинации"""
        self.logger.debug("Check pagination")
        try:
            pagination = self.get_elements(self.PAGINATION)
            if len(pagination) > 0:
                page_after_1 = self.get_elements(self.PAGE_NUM_AFT_1)
                num_of_page = len(page_after_1)
                if num_of_page == 1:
                    PAGE_PATH = By.XPATH, f'//*[@href="/network/access-point/index/?page=2"]'
                    self.click(PAGE_PATH)
                    self.click(self.ICON_RIGHT)
                    self.click(self.ICON_LEFT)
                else:
                    n = random.randint(2, num_of_page + 1)
                    PAGE_PATH = By.XPATH, f'//*[@href="/network/access-point/index/?page={n}"]'
                    self.click(PAGE_PATH)
                    self.click(self.ICON_RIGHT)
                    self.click(self.ICON_LEFT)
            else:
                pass
        except TimeoutException:
            pass

    def check_data_block_in_lk(self):
        """Проверка основного блока данных о точке доступа"""
        self.logger.debug("Gheck data block in lk")
        self.get_element(self.DATA_BLOCK_NAME)
        self.get_element(self.DATA_BLOCK_MAC)
        self.get_element(self.DATA_BLOCK_VENDOR)
        self.get_element(self.DATA_BLOCK_MODEL)
        self.get_element(self.DATA_BLOCK_SN)
        self.get_element(self.DATA_BLOCK_STATUS)
        self.get_element(self.DATA_BLOCK_TIS)
        self.get_element(self.DATA_BLOCK_DESCR)

    def check_hotspot_table(self):
        """Проверка полей в таблице связанных сетей"""
        self.logger.debug("Check hotspot table in lk")
        self.get_element(self.HOTSPOT_BLOCK)
        self.get_element(self.HSBLOCK_SERVICE)
        self.get_element(self.HSBLOCK_SSID)
        self.get_element(self.HSBLOCK_TYPE)
        self.get_element(self.HSBLOCK_REG)
        self.get_element(self.HSBLOCK_ADDR)

    def check_url(self, url_bc):
        url_before_check = url_bc
        url_after_check = self.browser.current_url
        if url_before_check == url_after_check:
            pass
        else:
            raise ValueError("Error: Url was changed")
