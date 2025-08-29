import allure
import pytest

from helpers.application_manager.application_manager import vsk


@allure.epic('Навигация по веб-приложению')
@allure.feature('Навигация по веб-приложению через хедер меню')
class TestNavigateHeaderMenu:

    @allure.story('Переход на страницу "Клиентам" (главная страница)')
    @allure.title('Проверка перехода на страницу "Клиентам" через хедер меню')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.smoke
    @pytest.mark.web
    @pytest.mark.fast
    def test_transition_to_clients_page(self):
        vsk.clients_page \
            .open() \
            .is_opened()

    @allure.story('Переход на страницу "Бизнесу"')
    @allure.title('Проверка перехода на страницу "Бизнесу" через хедер меню')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.smoke
    @pytest.mark.web
    @pytest.mark.fast
    def test_transition_to_business_page(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.header_menu.click_business()
        vsk.business_page.is_opened()

    @allure.story('Переход на страницу "Карьера"')
    @allure.title('Проверка перехода на страницу "Карьера" через хедер меню')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.smoke
    @pytest.mark.web
    @pytest.mark.fast
    def test_transition_to_career_page(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.header_menu.click_career()
        vsk.career_page.is_opened()

    @allure.story('Переход на страницу "Офисы"')
    @allure.title('Проверка перехода на страницу "Офисы" через хедер меню')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.smoke
    @pytest.mark.web
    @pytest.mark.fast
    def test_transition_to_offices_page(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.header_menu.click_offices()
        vsk.offices_page.is_opened()
