import allure

from helpers.application_manager.application_manager import vsk


@allure.epic('Полисы группы здоровья')
@allure.feature('На странице "Клиентам" отображается секция "Здоровье" с услугами')
class TestHealthServices:

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка переключения между группами услуг для страхования здоровья')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_switch_groups_in_health_section(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_season_group() \
            .click_accidents_group() \
            .click_critical_diseases_group() \
            .click_about_health_group()

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Антиклещ" в группе "Сезон"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_antiklesch_is_displayed_in_season_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_season_group() \
            .check_service_is_displayed(service_name='Антиклещ')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Дети" в группе "Несчастные случаи"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_children_is_displayed_in_accidents_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_accidents_group() \
            .check_service_is_displayed(service_name='Дети')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Взрослые" в группе "Несчастные случаи"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_adults_is_displayed_in_accidents_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_accidents_group() \
            .check_service_is_displayed(service_name='Взрослые')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Семья" в группе "Несчастные случаи"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_family_is_displayed_in_accidents_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_accidents_group() \
            .check_service_is_displayed(service_name='Семья')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Медицина без границ" в группе "Критические заболевания"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_medicine_without_borders_is_displayed_in_critical_diseases_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_critical_diseases_group() \
            .check_service_is_displayed(service_name='Медицина без границ')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Курс здоровья. Airflow" в группе "Про здоровье"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_airflow_is_displayed_in_about_health_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_about_health_group() \
            .check_service_is_displayed(service_name='Курс здоровья. Airflow')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Телемедицина" в группе "Про здоровье"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_telemedicine_is_displayed_in_about_health_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_about_health_group() \
            .check_service_is_displayed(service_name='Телемедицина')

    @allure.story('Услуги страхования здоровья')
    @allure.title('Проверка наличия услуги "Курс здоровья. Инвитро" в группе "Про здоровье"')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag('UI', 'WEB')
    @allure.label('owner', 'QAQ Falin Pavel')
    def test_that_service_invitro_is_displayed_in_about_health_group(self):
        vsk.clients_page \
            .open() \
            .is_opened()
        vsk.health_section \
            .click_health_section() \
            .section_is_opened() \
            .click_about_health_group() \
            .check_service_is_displayed(service_name='Курс здоровья. Инвитро')
