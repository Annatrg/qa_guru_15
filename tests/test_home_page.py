import allure
from helpers.home_page import HomePageHelper
from helpers.universal import UniversalHelper

home_page = HomePageHelper()
universal_helper = UniversalHelper()


@allure.title("Проверка наличия баннеров")
def test_banners():
    with allure.step('Открыть домашнюю страницу'):
        home_page.open_home_page()
    with allure.step('Проверить URL страницы'):
        universal_helper.check_url('https://www.ptsecurity.com/ru-ru/')
    with allure.step('Проверить, что на странице отображаются баннеры'):
        home_page.check_banners_is_visible()


@allure.title("Принять все cookies")
def test_cookies():
    with allure.step('Открыть домашнюю страницу'):
        home_page.open_home_page()
    with allure.step('Принять все куки'):
        home_page.accept_cookies()


@allure.title("Возвращение на главную страницу")
def test_go_to_home_page():
    with allure.step('Открыть любую страницу страницу'):
        universal_helper.open_page('/about/contacts/')
    with allure.step('Вернуться на домашнюю страницу через иконку логотипа'):
        universal_helper.return_home_page()
    with allure.step('Проверить URL страницы'):
        universal_helper.check_url('https://www.ptsecurity.com/ru-ru/')
