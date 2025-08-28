import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class OfficesPage:
    def __init__(self):
        self.url = Links.OFFICES_PAGE

    @allure.step('Открытие страницы "Офисы"')
    def open(self) -> 'OfficesPage':
        with allure.step(f'Открытие страницы: {self.url}'):
            browser.open(self.url)
        return self

    @allure.step('Проверка открытия страницы "Офисы"')
    def is_opened(self) -> 'OfficesPage':
        with allure.step(f'Проверка что страница {self.url} открыта'):
            browser.element('//h1[@class="h1-bold title"]').should(Condition.by_and(
                be.visible, have.text('Выберите город')))
        return self
