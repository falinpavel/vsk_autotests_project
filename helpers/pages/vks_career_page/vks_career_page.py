import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class CareerPage:
    def __init__(self):
        self.url = Links.CAREER_PAGE

    @allure.step('Открытие страницы "Карьера"')
    def open(self) -> 'CareerPage':
        with allure.step(f'Открытие страницы: {self.url}'):
            browser.open(self.url)
        return self

    @allure.step('Проверка открытия страницы "Карьера"')
    def is_opened(self) -> 'CareerPage':
        with allure.step(f'Проверка что страница {self.url} открыта'):
            browser.element('//h1[@class="page-title"]').should(Condition.by_and(
                be.visible, have.text('Свобода создавать будущее')))
        return self
