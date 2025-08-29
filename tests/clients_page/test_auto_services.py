import allure
import pytest

from helpers.application_manager.application_manager import vsk


@allure.epic('Полисы авто')
@allure.feature('На странице "Клиентам" отображается секция "Авто" с услугами')
class TestAutoServices:

    @allure.story('Услуги страхования авто')
    @allure.title('Проверка наличия услуги страхования "ОСАГО"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.web
    @pytest.mark.slow
    @pytest.mark.regression
    def test_that_policy_osago_is_displayed(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.auto_section \
            .click_auto_section() \
            .section_is_opened() \
            .check_service_is_displayed(service_name='ОСАГО')

    @allure.story('Услуги страхования авто')
    @allure.title('Проверка наличия услуги страхования "Каско"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.web
    @pytest.mark.slow
    @pytest.mark.regression
    def test_that_policy_casco_is_displayed(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.auto_section \
            .click_auto_section() \
            .section_is_opened() \
            .check_service_is_displayed(service_name='Каско')

    @allure.story('Услуги страхования авто')
    @allure.title('Проверка наличия услуги страхования "Каско компакт минимум"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.web
    @pytest.mark.slow
    @pytest.mark.regression
    def test_that_policy_casco_compact_minimum_is_displayed(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.auto_section \
            .click_auto_section() \
            .section_is_opened() \
            .check_service_is_displayed(service_name='Каско компакт минимум')

    @allure.story('Услуги страхования авто')
    @allure.title('Проверка наличия услуги страхования "Международные системы страхования"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.web
    @pytest.mark.slow
    @pytest.mark.regression
    def test_that_policy_transnational_systems_is_displayed(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.auto_section \
            .click_auto_section() \
            .section_is_opened() \
            .check_service_is_displayed(service_name='Международные системы страхования')

    @allure.story('Услуги страхования авто')
    @allure.title('Проверка наличия услуги страхования "ОСГОП"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    @pytest.mark.web
    @pytest.mark.slow
    @pytest.mark.regression
    def test_that_policy_osgop_is_displayed(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.auto_section \
            .click_auto_section() \
            .section_is_opened() \
            .check_service_is_displayed(service_name='ОСГОП')
