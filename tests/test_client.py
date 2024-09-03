import allure
import pytest
from page_object.access_list_page import AccessListPage
from page_object.access_point_page import ApPage
from page_object.adm_page_check import AdminPage
from page_object.login_page import LoginPage
from page_object.header_and_footer_element import HeaderElement
from page_object.main_page import MainPage
from page_object.modal_survey_page import ModalSurveyPage
from page_object.poll_page import PollPage
from page_object.profile_page import ProfilePage

username = "test_account@test.com"
username_uc = "TEST_ACCOUNT@TEST.COM"
password = "q1w2e3r4"
option_qual = 3


@allure.feature('client')
@allure.story('Авторизация В ЛК')
@allure.title('Авторизация в ЛК c email в разных регистрах')
def test_login_local(browser, stand):
    """Авторизация (разный регистр)"""
    login_page = LoginPage(browser)
    header_el = HeaderElement(browser)
    profile_page = ProfilePage(browser)
    modal_win = ModalSurveyPage(browser)
    login_page.local_login(stand, username, password)
    modal_win.close_modal_win()
    header_el.click_profile_button()
    profile_page.search_profile_title()
    profile_page.get_text_by_path(text=username)
    header_el.click_logout_button()
    login_page.local_login(stand, username_uc, password)
    modal_win.close_modal_win()
    header_el.click_profile_button()
    profile_page.search_profile_title()
    profile_page.get_text_by_path(text=username)
    header_el.click_logout_button()


@allure.feature('client')
@allure.story('Авторизация в ЛК')
@allure.title('Авторизация в ЛК через RT Passport')
@pytest.mark.parametrize(("username", "password"),
                         [
                             ('pre_account@pre.com', 'Q1w2e3r4')
                         ])
def test_login_sso(browser, stand, username, password):
    """Авторизация через SSO"""
    login_page = LoginPage(browser)
    header_el = HeaderElement(browser)
    profile_page = ProfilePage(browser)
    modal_win = ModalSurveyPage(browser)
    if stand == 'dev':
        pass
    elif stand in ['test', 'pre']:
        login_page.sso_login(username, password)
        modal_win.close_modal_win()
        header_el.click_profile_button()
        profile_page.search_profile_title()
        profile_page.get_text_by_path(text=username)
        header_el.click_logout_button()
    else:
        raise ValueError("Error: Stand not supported")


@allure.feature('client')
@allure.story('ЛК/Оборудование/Точки доступа')
@allure.title('Просмотр карточки точки доступа в ЛК')
def test_access_point_view_in_lk(browser, stand, login_type):
    """Просмотр карточки точки доступа в ЛК"""
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    ap_page = ApPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    main_page.open_access_points_page()
    ap_page.check_ap_service_in_table_on_mian_ap_page()
    ap_page.check_ap_status_in_table_on_main_ap_page()
    ap_page.check_pagination()
    ap_page.click_on_random_table_row()
    ap_page.check_data_block_in_lk()
    ap_page.check_hotspot_table()
    url = main_page.get_url()
    ap_page.click_on_first_table_row()
    ap_page.check_url(url)
    ap_page.check_ap_service_in_table_on_ap_page()
    ap_page.check_hs_type_in_table_on_ap_page()


@allure.feature('client')
@allure.story('ЛК/Опросы')
@allure.title('Добавление опроса с одиночным выбором')
def test_add_single_poll(browser, stand, login_type):
    """Добавление опроса с одиночным выбором"""
    filter_object = 'Опрос'
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    poll_page = PollPage(browser)
    adm_page = AdminPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    url = main_page.get_url()
    main_page.open_poll_page()
    poll_page.click_on_add_new_poll_button()
    poll_page.chose_single_type()
    poll_name = poll_page.input_base_field()
    poll_page.add_opt_filed_for_n(option_qual)
    poll_page.poll_imp_manage()
    poll_page.poll_imp_manage_allow_repeat()
    poll_page.poll_imp_manage_allow_skip()
    poll_page.poll_imp_manage_by_date()
    poll_page.click_poll_save_button()
    poll_page.check_name_after_create(poll_name=poll_name)
    poll_page.edit_first_poll()
    path = main_page.get_path(url)
    adm_url = adm_page.get_adm_url(url)
    adm_page.check_changes_in_audit(adm_url, filter_object, path)


@allure.feature('client')
@allure.story('ЛК/Опросы')
@allure.title('Добавление опроса с множественным выбором')
def test_add_multiple_poll(browser, stand, login_type):
    """Добавление опроса с множественным выбором"""
    filter_object = 'Опрос'
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    poll_page = PollPage(browser)
    adm_page = AdminPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    url = main_page.get_url()
    main_page.open_poll_page()
    poll_page.click_on_add_new_poll_button()
    poll_page.chose_multiple_type()
    poll_name = poll_page.input_base_field()
    poll_page.add_opt_filed_for_n(option_qual)
    poll_page.poll_imp_manage()
    poll_page.poll_imp_manage_allow_repeat()
    poll_page.poll_imp_manage_allow_skip()
    poll_page.poll_imp_manage_by_date()
    poll_page.click_poll_save_button()
    poll_page.check_name_after_create(poll_name=poll_name)
    poll_page.edit_first_poll()
    path = main_page.get_path(url)
    adm_url = adm_page.get_adm_url(url)
    adm_page.check_changes_in_audit(adm_url, filter_object, path)


@allure.feature('client')
@allure.story('ЛК/Опросы')
@allure.title('Добавление рейтингого опроса')
def test_add_rating_poll(browser, stand, login_type):
    """Добавление рейтингого опроса"""
    filter_object = 'Опрос'
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    poll_page = PollPage(browser)
    adm_page = AdminPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    url = main_page.get_url()
    main_page.open_poll_page()
    poll_page.click_on_add_new_poll_button()
    poll_page.chose_rating_type()
    poll_name = poll_page.input_base_field()
    poll_page.poll_imp_manage()
    poll_page.poll_imp_manage_allow_repeat()
    poll_page.poll_imp_manage_allow_skip()
    poll_page.poll_imp_manage_by_votes()
    poll_page.click_poll_save_button()
    poll_page.check_name_after_create(poll_name=poll_name)
    poll_page.edit_first_poll()
    path = main_page.get_path(url)
    adm_url = adm_page.get_adm_url(url)
    adm_page.check_changes_in_audit(adm_url, filter_object, path)


@allure.feature('client')
@allure.story('ЛК/Доступ по спискам')
@allure.title('Добавление телефонного номера в разделе Доступ по спискам')
def test_add_access_list(browser, stand, login_type):
    """Добавление телефонного номера"""
    filter_object = 'Доступ по списку'
    ssid_ids = [6568, 6573, 6651]
    comment = "Комментарий"
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    acc_list_page = AccessListPage(browser)
    adm_page = AdminPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    url = main_page.get_url()
    main_page.open_access_list_page()
    acc_list_page.click_on_add_new_acc_list_button()
    phone = acc_list_page.generate_phone_number()
    acc_list_page.input_phone_number(phone)
    acc_list_page.select_active_status()
    acc_list_page.select_hotspots_by_ids(ssid_ids=ssid_ids)
    acc_list_page.input_comment(comment=comment)
    acc_list_page.save_phone()
    acc_list_page.check_phone_on_main_acc_list_page(phone)
    acc_list_page.open_first_phone()
    acc_list_page.check_hotspots_on_phone_page(ssid_ids)
    path = main_page.get_path(url)
    adm_url = adm_page.get_adm_url(url)
    adm_page.check_changes_in_audit(adm_url, filter_object, path)


@allure.feature('client')
@allure.story('ЛК/Доступ по спискам')
@allure.title('Форма просмотра телефонного номера в списке')
def test_view_phone_in_access_list(browser, stand, login_type):
    """Форма просмотра телефонного номера в списке"""
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    acc_list_page = AccessListPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    main_page.open_access_list_page()
    acc_list_page.open_first_phone()
    acc_list_page.check_data_block_in_lk()
    acc_list_page.check_hotspots_block_in_lk()
    acc_list_page.check_pagination()


# @allure.feature('client')  #Не запускался из-за ошибки
# @allure.story('ЛК/Доступ по спискам')
# @allure.title('Форма просмотра списка телефонных номеров')
# def test_view_access_list_main_page(browser, stand, login_type):
#     """Форма просмотра списка телефонных номеров"""
#     login_page = LoginPage(browser)
#     modal_win = ModalSurveyPage(browser)
#     main_page = MainPage(browser)
#     acc_list_page = AccessListPage(browser)
#     if login_type == 'local':
#         login_page.local_login(stand, username, password)
#     elif login_type == 'sso':
#         login_page.sso_login(username, password)
#     else:
#         raise ValueError("Error: Login type not supported")
#     modal_win.close_modal_win()
#     main_page.open_access_list_page()
#     acc_list_page.check_phone_table_on_mp_in_lk()
#     acc_list_page.check_phone_status_in_table_on_mian_ap_page()
#     phone = acc_list_page.get_first_phone()
#     acc_list_page.check_search_phone(phone)
#     comment = acc_list_page.get_first_comment()
#     acc_list_page.check_search_by_comment(comment)
#     acc_list_page.check_search_by_non_existent_value()
#     acc_list_page.open_first_phone()
#     main_page.go_back()
#     acc_list_page.check_pagination()


@allure.feature('client')
@allure.story('ЛК/Доступ по спискам')
@allure.title('Редактирование телефонного номера')
def test_edit_first_phone_on_access_list(browser, stand, login_type):
    """Редактирование телефонного номера"""
    filter_object = 'Доступ по списку'
    login_page = LoginPage(browser)
    modal_win = ModalSurveyPage(browser)
    main_page = MainPage(browser)
    acc_list_page = AccessListPage(browser)
    adm_page = AdminPage(browser)
    if login_type == 'local':
        login_page.local_login(stand, username, password)
    elif login_type == 'sso':
        login_page.sso_login(username, password)
    else:
        raise ValueError("Error: Login type not supported")
    modal_win.close_modal_win()
    url = main_page.get_url()
    main_page.open_access_list_page()
    phone_old = acc_list_page.get_first_phone()
    comment_old = acc_list_page.get_first_comment()
    acc_list_page.open_first_phone()
    acc_list_page.edit_phone()
    acc_list_page.check_field_on_edit_page()
    phone_1 = acc_list_page.generate_phone_number()
    acc_list_page.input_phone_number(phone_1)
    acc_list_page.del_last_hotspot_in_dd()
    acc_list_page.input_random_comment()
    acc_list_page.cancel_saving_phone()
    acc_list_page.check_phone_with_7(phone_old)
    phone_2 = acc_list_page.generate_phone_number()
    acc_list_page.edit_phone()
    acc_list_page.input_phone_number(phone_2)
    acc_list_page.save_phone()
    acc_list_page.check_phone_without_7(phone_2)
    hs_q_old = acc_list_page.get_hs_quantity()
    acc_list_page.edit_phone()
    acc_list_page.del_last_hotspot_in_dd()
    acc_list_page.save_phone()
    hs_q_new = acc_list_page.get_hs_quantity()
    acc_list_page.check_hotspots(hs_q_old, hs_q_new)
    acc_list_page.edit_phone()
    comment_new = acc_list_page.input_random_comment()
    acc_list_page.save_phone()
    acc_list_page.check_comments(comment_old, comment_new)
    path = main_page.get_path(url)
    adm_url = adm_page.get_adm_url(url)
    adm_page.check_changes_in_audit(adm_url, filter_object, path)
