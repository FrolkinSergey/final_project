import allure
from page_object.alert_element import AlertElement
from page_object.catalog_page import CatalogPage
from page_object.header_and_footer_element import HeaderElement
from page_object.admin_page import AdminPage
from page_object.main_page import MainPage


@allure.feature('HW3')
@allure.story('Refactoring HW1, Part 3')
@allure.title('Авторизация, проверка авторизации, выход из админки')
def test_login_and_check_and_logout(browser):
    """Авторизация, проверка авторизации, выход из админки"""
    username = "user"
    password = "bitnami"
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login(username, password)
    admin_page.get_logout_button()
    admin_page.logout()
    admin_page.get_username_input_field()
    admin_page.get_password_input_field()


@allure.feature('HW3')
@allure.story('Refactoring HW1, Part 3')
@allure.title('Добавление товара в корзину')
def test_add_to_cart(browser):
    """Добавление товара в корзину и проверка его наличия в ней"""
    main_p = MainPage(browser)
    header_el = HeaderElement(browser)
    alert_el = AlertElement(browser)
    header_el.click_cart_hidden()
    header_el.check_empty_cart()
    header_el.click_cart_show()
    main_p.add_to_cart_first_product_of_featured()
    alert_el.get_success_alert()
    header_el.click_cart_hidden()
    header_el.get_elements_in_cart_with_added_product()


@allure.feature('HW3')
@allure.story('Refactoring HW1, Part 3')
@allure.title('Проверка изменения цены на товары на главной странице')
def test_price_on_main_page(browser):
    """Проверка изменения цены на товары на главной странице через сранение цен"""
    main_p = MainPage(browser)
    header_el = HeaderElement(browser)
    p_new1 = main_p.get_price_of_any_product_main()
    header_el.click_change_euro()
    p: str = p_new1
    p_new2 = main_p.get_price_of_any_product_main()
    assert p != p_new2.text


@allure.feature('HW3')
@allure.story('Refactoring HW1, Part 3')
@allure.title('Проверка изменения цены на товары на странице каталога')
def test_price_on_catalog_page(browser):
    """Проверка изменения цены на товары на странице каталога через сранение цен"""
    header_el = HeaderElement(browser)
    cat_p = CatalogPage(browser)
    header_el.click_any_dropdown()
    header_el.click_show_all()
    p_new3 = cat_p.get_price_of_any_product_catalog()
    header_el.click_change_euro()
    p: str = p_new3
    p_new4 = cat_p.get_price_of_any_product_catalog()
    assert p != p_new4.text
