import random
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class PollPage(BasePage):
    ADD_BUTTON = By.XPATH, '//*[@class="btn btn-primary btn-icon"]'
    POLL_NAME = By.CSS_SELECTOR, "#poll-name"
    POLL_GREET = By.CSS_SELECTOR, "#poll-greeting"
    POLL_QNAME = By.CSS_SELECTOR, "#poll-question-name-0"
    POLL_TYPE_DD = By.XPATH, '//*[@id="poll-app"]/form/div[1]/div/div[1]/div/div[1]/fieldset/div[3]/div/div/div[1]/div[2]/div/div[1]'
    POLL_TYPE_SINGLE = By.XPATH, '//*[@data-id="SINGLE"]'
    POLL_TYPE_MULTIPLE = By.XPATH, '//*[@data-id="MULTIPLE"]'
    POLL_TYPE_RATING = By.XPATH, '//*[@data-id="RATING"]'
    POLL_OPT_ADD_BUTTON = By.XPATH, '//*[@class="btn btn-primary-outline btn-sm"]'
    POLL_ENDING_TEXT = By.CSS_SELECTOR, "#poll-ending"
    POLL_SAVE_BUTTON = By.XPATH, '//*[@class="btn btn-primary ml-2"]'
    POLL_IMP_MANAGE = By.XPATH, "//*[contains(text(),'Управление показами')]"
    POLL_END_BY_DATE = By.CSS_SELECTOR, "#check-end-date"
    POLL_CANELDAR = By.XPATH, '//*[@class="custom-input-action custom-input-default-icon"]'
    POLL_CURRENTDATE = By.XPATH, f'//*[@data-d="{str(datetime.now().day)}"]'
    POLL_END_BY_VOTES = By.CSS_SELECTOR, "#check-end-votes"
    POLL_ENDDATE_FIELD = By.XPATH, "//*[contains(text(),' Дата окончания ')]"
    POLL_ENDVOTES_FIELD = By.XPATH, '//*[@type="number"]'
    POLL_ALLOW_REPEAT = By.XPATH, '//*[@id="allow-repeat"]'
    POLL_ALLOW_SKIP = By.XPATH, '//*[@id="allow-skip"]'
    POLL_EDIT = By.XPATH, '//*[@class="btn btn-sm btn-icon"]'

    def click_on_add_new_poll_button(self):
        """Нажатие кнопки +Добавить опрос"""
        self.logger.info("Click add new poll button")
        self.click(self.ADD_BUTTON)

    def input_base_field(self):
        """Заполнение полей, одинаковых для 3 типов опросов"""
        self.logger.info("Input required field")
        currentday = datetime.now().strftime("%d")
        currentmonth = datetime.now().strftime("%m")
        currentyear = datetime.now().strftime("%Y")
        now = datetime.now().strftime("%H:%M:%S")
        name = "Autotest Poll " + "{year}.{month}.{day}" + ":" + now
        time_name = name.format(year=currentyear, month=currentmonth, day=currentday)
        self.input_value(self.POLL_NAME, time_name)
        self.input_value(self.POLL_GREET, "Приветствие")
        self.input_value(self.POLL_QNAME, "Вопрос")
        self.input_value(self.POLL_ENDING_TEXT, "Спасибо!")
        return time_name

    def add_opt_filed_for_n(self, n):
        """Добавление полей вариантов"""
        self.logger.info("Add opt field")
        option_qual = n - 1
        for i in range(option_qual):
            POLL_OPT_NAME_I = By.CSS_SELECTOR, f"#poll-option-name-0-{i}"
            self.input_value(POLL_OPT_NAME_I, f"Вариант {i}")
            if i == option_qual:
                pass
            else:
                try:
                    self.click(self.POLL_OPT_ADD_BUTTON)
                except TimeoutException:
                    pass
        POLL_OPT_NAME_I1 = By.CSS_SELECTOR, f"#poll-option-name-0-{option_qual}"
        self.input_value(POLL_OPT_NAME_I1, f"Вариант {option_qual}")

    def chose_single_type(self):
        """Тип - Одиночный выбор"""
        self.logger.info("Chose single type")
        self.click(self.POLL_TYPE_DD)
        self.click(self.POLL_TYPE_SINGLE)

    def chose_multiple_type(self):
        """Тип - Множественный выбор"""
        self.logger.info("Chose multiple type")
        self.click(self.POLL_TYPE_DD)
        self.click(self.POLL_TYPE_MULTIPLE)

    def chose_rating_type(self):
        """Тип - Рейтинг"""
        self.logger.info("Chose rating type")
        self.click(self.POLL_TYPE_DD)
        self.click(self.POLL_TYPE_RATING)

    def click_poll_save_button(self):
        """Сохранение опроса"""
        self.logger.info("Save poll")
        self.click(self.POLL_SAVE_BUTTON)

    def poll_imp_manage(self):
        """Открытие вклдаки Управление опросами"""
        self.logger.info("Save poll")
        self.click(self.POLL_IMP_MANAGE)

    def poll_imp_manage_allow_repeat(self):
        """Установить чек-бокс Повторное прохождение"""
        self.logger.info("Allow repeat")
        self.click(self.POLL_ALLOW_REPEAT)

    def poll_imp_manage_allow_skip(self):
        """Установить чек-бокс Разрешить пропуск"""
        self.logger.info("Allow skip")
        self.click(self.POLL_ALLOW_SKIP)

    def poll_imp_manage_by_date(self):
        """Заполнение вклдаки Управление опросами завершение по дате"""
        self.logger.info("End by date")
        self.click(self.POLL_END_BY_DATE)
        callendars = self.get_elements(self.POLL_CANELDAR)
        ebd_calendar = callendars[1]
        ebd_calendar.click()
        cur_date_in_ebd_calendar = self.get_elements(self.POLL_CURRENTDATE)
        cur_date = cur_date_in_ebd_calendar[1]
        cur_date.click()

    def poll_imp_manage_by_votes(self):
        """Заполнение вклдаки Управление опросами завершение по количеству ответов"""
        self.logger.info("End by votes")
        self.click(self.POLL_END_BY_VOTES)
        votes = str(random.randint(2, 10))
        self.input_value(self.POLL_ENDVOTES_FIELD, votes)

    def check_name_after_create(self, poll_name):
        """Проверка наличия опроса в разделе Опросы"""
        self.logger.info("Check name after create")
        POLL_NAME_ON_POLLMAINPAGE = By.XPATH, f'//*[@data-original-title="{poll_name}"]'
        self.get_element(POLL_NAME_ON_POLLMAINPAGE)

    def edit_first_poll(self):
        """Редактирование последнего опроса"""
        self.logger.info("Edit first poll")
        edit_buttons = self.get_elements(self.POLL_EDIT)
        buttons = len(edit_buttons)
        for i in range(buttons):
            first_edit_button = edit_buttons[i]
            attr = first_edit_button.get_attribute('tittle')
            if attr == 'Архивировать':
                pass
            else:
                first_edit_button.click()
                break
