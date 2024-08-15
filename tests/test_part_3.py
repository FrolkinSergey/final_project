import allure
from page_object.admin_page import AdminPage
from page_object.alert_element import AlertElement
from page_object.header_and_footer_element import HeaderElement
from page_object.main_page import MainPage
from page_object.registration_page import RegistrationPage


@allure.feature('HW3')
@allure.story('Refactoring HW2')
@allure.title('Создание нового продукта в админке')
def test_create_new_product_in_admin_page(browser):
    """Создание нового продукта в админке по заданным параметрам"""
    username = "user"
    password = "bitnami"
    product_name = "New Product 9999"
    meta_title = "12345678"
    model = "Unknown 7"
    default = "new-product9999" #без пробелов
    al_el = AlertElement(browser)
    adm_p = AdminPage(browser)
    adm_p.open()
    adm_p.login(username, password)
    adm_p.open_products()
    adm_p.click_add_new_product()
    adm_p.input_required_field(product_name, meta_title, model, default)
    al_el.get_success_alert()


@allure.feature('HW3')
@allure.story('Refactoring HW2')
@allure.title('Удаление первого продукта в админке')
def test_delete_product_in_admin_page(browser):
    """Удаление первого продукта в админке после авторизации"""
    username = "user"
    password = "bitnami"
    al_el = AlertElement(browser)
    adm_p = AdminPage(browser)
    adm_p.open()
    adm_p.login(username, password)
    adm_p.open_products()
    adm_p.choice_checkbox_1()
    adm_p.click_delete()
    adm_p.accept_alert()
    al_el.get_success_alert()


@allure.feature('HW3')
@allure.story('Refactoring HW2')
@allure.title('Создание нового пользователя')
def test_add_new_user(browser):
    """Создание нового пользователя по заданным параметрам"""
    first_name = "Serg"
    last_name = "Frolkin"
    email = "testfrolkin@gmail.com"
    password = "PasswordIdeal67"
    reg_p = RegistrationPage(browser)
    reg_p.open()
    reg_p.register_page_input_value(first_name, last_name, email, password)
    reg_p.enter_checkboxes()
    reg_p.click_continue()
    reg_p.check_registration()


@allure.feature('HW3')
@allure.story('Refactoring HW2')
@allure.title('Проверка изменения цены на товары')
def test_change_currency(browser):
    """Проверка изменения цены на товары при переключении валют"""
    main_p = MainPage(browser)
    header_el = HeaderElement(browser)
    p_1 = main_p.get_price_of_any_product_main()
    header_el.click_change_euro()
    p1: str = p_1
    p_2 = main_p.get_price_of_any_product_main()
    header_el.click_change_pound()
    p2: str = p_2
    p_3 = main_p.get_price_of_any_product_main()
    header_el.click_change_dollar()
    p3: str = p_3
    assert p1 != p2 != p3
