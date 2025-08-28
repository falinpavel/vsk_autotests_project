import os

from dotenv import load_dotenv

load_dotenv()


class Links:
    """
    Класс содержит ссылки на все страницы сайта
    """
    CLIENTS_PAGE = f"{os.getenv('BASE_URL')}/klientam"

    BUSINESS_PAGE = f"{os.getenv('BASE_URL')}/biznesu"

    CAREER_PAGE = f"{os.getenv('BASE_URL')}/klientam/karyera"

    OFFICES_PAGE = f"{os.getenv('BASE_URL')}/klientam/offices"


