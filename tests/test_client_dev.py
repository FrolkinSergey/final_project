import allure
from page_object.login_page import LoginPage
from page_object.header_and_footer_element import HeaderElement
from page_object.profile_page import ProfilePage

username_classic2 = "vaseteg945@gam1fy.com"
username_classic2_UC = "VASETEG945@GAM1FY.COM"
password_classic2 = "q1w2e3r4"


@allure.feature('client')
@allure.story('Refactoring HW1, Part 3')
@allure.title('Авторизация в ЛК, выход + проверка')
def test_lk_login_logout_check(browser):
    """Авторизация в ЛК + выход (арзный регистр)"""
    login_page = LoginPage(browser)
    header_el = HeaderElement(browser)
    profile_page = ProfilePage(browser)
    login_page.open()
    header_el.get_navbar_brand()
    login_page.login(username_classic2, password_classic2)
    header_el.click_profile_button()
    profile_page.search_profile_title()
    header_el.click_logout_button()
    login_page.login(username_classic2_UC, password_classic2)
    header_el.click_profile_button()
    profile_page.search_profile_title()
    header_el.click_logout_button()
