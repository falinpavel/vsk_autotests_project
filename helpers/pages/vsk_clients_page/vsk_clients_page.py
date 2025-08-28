import allure
from selene import browser, be, have
from selene.core.condition import Condition

from helpers.data.links import Links


class ClientsPage:
    """
    Класс главной страницы сайта.
    Описывает методы для работы с главной страницей
    (за исключением хедер меню, методы работы с этим компонентом вынесены в отдельный Page Object.)
    """
    def __init__(self):
        self.url = Links.CLIENTS_PAGE

    @allure.step('Открытие главной страницы (страница "Клиенты")')
    def open(self) -> 'ClientsPage':
        with allure.step(f'Открытие главной страницы: {self.url}'):
            browser.open(self.url)
        return self

    @allure.step('Проверка открытия главной страницы')
    def is_opened(self) -> 'ClientsPage':
        with allure.step(f'Проверка что главная страница (страница "Клиенты") {self.url} открыта'):
            browser.element('//h1[@class="title"]').should(Condition.by_and(be.visible, have.text('Главное')))
        return self
