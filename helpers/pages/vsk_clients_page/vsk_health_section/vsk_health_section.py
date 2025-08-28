import allure
from selene import browser, be, have, command
from selene.core.condition import Condition


class HealthSection:
    @allure.step('Открытие секции "Здоровье"')
    def click_health_section(self) -> 'HealthSection':
        with allure.step(f'Находясь на странице "Клиентам" нажать на секцию "Здоровье"'):
            browser.element('#health').should(Condition.by_and(be.clickable, have.text('Здоровье'))).click()
        return self

    @allure.step('Проверка открытия секции "Здоровье"')
    def section_is_opened(self) -> 'HealthSection':
        with allure.step(f'Проверка открытия секции "Здоровье" по тексту на странице'):
            browser.element('//h1[@class="title"]').should(Condition.by_and(be.visible, have.text('Здоровье')))
        return self

    @allure.step('Проверка наличия услуги в секции "Здоровье"')
    def check_service_is_displayed(self, service_name: str) -> 'HealthSection':
        with allure.step(f'Проверить что услуга {service_name} отображена на странице'):
            browser.element(f'//h4[@class="title" and text()=" {service_name} "]').perform(
                command.js.scroll_into_view).should(Condition.by_and(be.visible, have.text(service_name)))
        return self

    @allure.step('В секции "Здоровье" нажать на группу "Сезон"')
    def click_season_group(self) -> 'HealthSection':
        with allure.step(f'В секции "Здоровье" нажать на группу "Сезон"'):
            browser.element('//a[@href="/klientam/zdorove?t=relevant"]').should(Condition.by_and(
                be.clickable, have.text('Сезон'))).click()
        return self

    @allure.step('В секции "Здоровье" нажать на группу "Несчастные случаи"')
    def click_accidents_group(self) -> 'HealthSection':
        with allure.step(f'В секции "Здоровье" нажать на группу "Несчастные случаи"'):
            browser.element('//a[@href="/klientam/zdorove?t=accidents"]').should(Condition.by_and(
                be.clickable, have.text('Несчастные случаи'))).click()
        return self

    @allure.step('В секции "Здоровье" нажать на группу "Критические заболевания"')
    def click_critical_diseases_group(self) -> 'HealthSection':
        with allure.step(f'В секции "Здоровье" нажать на группу "Критические заболевания"'):
            browser.element('//a[@href="/klientam/zdorove?t=criticalDiseases"]').should(Condition.by_and(
                be.clickable, have.text('Критические заболевания'))).click()
        return self

    @allure.step('В секции "Здоровье" нажать на группу "Про здоровье"')
    def click_about_health_group(self) -> 'HealthSection':
        with allure.step(f'В секции "Здоровье" нажать на группу "Про здоровье"'):
            browser.element('//a[@href="/klientam/zdorove?t=aboutHealth"]').should(Condition.by_and(
                be.clickable, have.text('Про здоровье'))).click()
        return self
