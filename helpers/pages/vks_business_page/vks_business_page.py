import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class BusinessPage:
    def __init__(self):
        self.url = Links.BUSINESS_PAGE

    @allure.step('Открытие страницы "Бизнесу"')
    def open(self) -> 'BusinessPage':
        with allure.step(f'Открытие страницы: {self.url}'):
            browser.open(self.url)
        return self

    @allure.step('Проверка открытия страницы "Бизнесу"')
    def is_opened(self) -> 'BusinessPage':
        with allure.step(f'Проверка что страница {self.url} открыта'):
            browser.element('//div[text()="Страхование корпоративных клиентов"]').should(Condition.by_and(be.visible))
        return self
