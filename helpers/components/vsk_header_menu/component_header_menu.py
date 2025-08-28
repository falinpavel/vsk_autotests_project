import allure

from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class ComponentHeaderMenu:
    """
    Класс компонента хедер меню. Описывает методы для работы с хедер меню.
    Возвращает объект класса ComponentHeaderMenu(паттерн Fluent Page Object).
    """
    @allure.step('Кликнуть и перейти на главную страницу (страница "Клиентам")')
    def click_clients(self) -> 'ComponentHeaderMenu':
        with allure.step(f'Переход по клику на страницу "Клиентам" по URL: {Links.CLIENTS_PAGE}'):
            browser.element('//a[@href="/klientam"]').should(Condition.by_and(
                be.clickable, have.text('Клиентам'))).click()
        return self

    @allure.step('Кликнуть и перейти на страницу "Бизнесу>"')
    def click_business(self) -> 'ComponentHeaderMenu':
        with allure.step(f'Переход по клику на страницу "Бизнесу" по URL: {Links.BUSINESS_PAGE}'):
            browser.element('//a[@href="/biznesu"]').should(Condition.by_and(
                be.clickable, have.text('Бизнесу'))).click()
        return self

    @allure.step('Кликнуть и перейти на страницу "Карьера"')
    def click_career(self) -> 'ComponentHeaderMenu':
        with allure.step(f'Переход по клику на страницу "Карьера" по URL: {Links.CAREER_PAGE}'):
            browser.element('//a[@href="/klientam/karyera" and @class="vsk-text-14-semi"]').should(Condition.by_and(
                be.clickable, have.text('Карьера'))).click()
        return self

    @allure.step('Кликнуть и перейти на страницу "Офисы"')
    def click_offices(self) -> 'ComponentHeaderMenu':
        with allure.step(f'Переход по клику на страницу "Офисы" по URL: {Links.OFFICES_PAGE}'):
            browser.element('//a[@href="/klientam/offices" and @class="vsk-text-14-semi"]').should(Condition.by_and(
                be.clickable, have.text('Офисы'))).click()
        return self
