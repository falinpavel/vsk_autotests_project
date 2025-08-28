from helpers.pages.vsk_clients_page.vsk_auto_section.vsk_auto_section import AutoSection
from helpers.pages.vsk_clients_page.vsk_clients_page import ClientsPage
from helpers.components.vsk_header_menu.component_header_menu import ComponentHeaderMenu
from helpers.pages.vks_business_page.vks_business_page import BusinessPage
from helpers.pages.vks_career_page.vks_career_page import CareerPage
from helpers.pages.vks_offices_page.vks_offices_page import OfficesPage
from helpers.pages.vsk_clients_page.vsk_health_section.vsk_health_section import HealthSection


class ApplicationManager:
    """
    Класс менеджера приложения который инкапсулирует в себе все Page Object и другие объекты,
    необходимые для взаимодействия с приложением. Как итог - любые страницы и компоненты доступны в любом тесте.
    """
    def __init__(self):
        self.header_menu = ComponentHeaderMenu()

        self.clients_page = ClientsPage()
        self.auto_section = AutoSection()
        self.health_section = HealthSection()

        self.business_page = BusinessPage()
        self.career_page = CareerPage()
        self.offices_page = OfficesPage()


vsk = ApplicationManager()
