import allure
from selene import browser, be, have, command
from selene.core.condition import Condition


class AutoSection:
    @allure.step('Открытие секции страхования "Авто"')
    def click_auto_section(self) -> 'AutoSection':
        with allure.step(f'Находясь на странице "Клиентам" нажать на секцию страхования "Авто"'):
            browser.element('#auto').should(Condition.by_and(be.clickable, have.text('Авто'))).click()
        return self

    @allure.step('Проверка открытия секции страхования "Авто"')
    def section_is_opened(self) -> 'AutoSection':
        with allure.step(f'Проверка открытия секции страхования "Авто" по тексту на странице'):
            browser.element('//h1[@class="title"]').should(Condition.by_and(be.visible, have.text('Полисы Авто')))
        return self

    @allure.step('Проверка наличия услуги в секции "Полисы Авто"')
    def check_service_is_displayed(self, service_name: str) -> 'AutoSection':
        with allure.step(f'Проверить что услуга {service_name} отображена на странице'):
            browser.element(f'//h4[@class="title" and text()=" {service_name} "]').perform(
                command.js.scroll_into_view).should(Condition.by_and(be.visible, have.text(service_name)))
        return self
