from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class CreatorOfVacancies(ABC):
    """
    абстрактный класс для приобразования инфы от api в класс Vacancy
    """
    @staticmethod
    @abstractmethod
    def make_vacancy(job: dict):
        pass


class CreatorFromHh(CreatorOfVacancies):

    @staticmethod
    def make_vacancy(job: dict) -> list:
        vacancy_instances = []  # список для хранения экземпляров
        vacancies = job['items']  # берет только информацию о вакансиях

        for vac in vacancies:

            vacancy = Vacancy()

            # каждую вакансию превращает в объект класса Vacancy, присваивая полям значения из словаря
            vacancy.name = vac['name']   # название вакансии
            vacancy.place = vac['area']['name']   # место работы территориально
            vacancy.salary_from = vac['salary']['from']
            vacancy.salary_to = vac['salary']['to']
            vacancy.salary_currency = vac['salary']['currency']
            vacancy.url = vac['alternate_url']

            # тут нужно поменять значение, если оно None, на пустую строку
            if vac['snippet']['requirement'] == None:
                vac['snippet']['requirement'] = ''
            if vac['snippet']['responsibility'] == None:
                vac['snippet']['responsibility'] = ''

            # требования и описания записывает в одно поле
            vacancy.description = vac['snippet']['requirement'] + '\n' + vac['snippet']['responsibility']
            vacancy.operating_mode = vac['employment']['name']

            # оставляет метку, где была взята вакансия
            vacancy.made_from = 'HeadHunter'

            # добавляет в экземпляр с заполненными полями в список и возвращает его
            vacancy_instances.append(vacancy)
        return vacancy_instances


class CreatorFromJs(CreatorOfVacancies):

    @staticmethod
    def make_vacancy(job: dict) -> list:
        vacancy_instances = []  # список для хранения экземпляров
        vacancies = job['objects']  # берет только информацию о вакансиях

        for vac in vacancies:
            vacancy = Vacancy()

            # каждую вакансию превращает в объект класса Vacancy, присваивая полям значения из словаря
            vacancy.name = vac['profession']   # название вакансии
            vacancy.place = vac['address']   # место работы территориально
            vacancy.salary_from = vac['payment_from']
            vacancy.salary_to = vac['payment_to']
            vacancy.salary_currency = vac['currency']
            vacancy.url = vac['link']
            vacancy.description = vac['candidat']
            vacancy.operating_mode = vac['type_of_work']['title']

            # оставляет метку, где была взята вакансия
            vacancy.made_from = 'SuperJob'

            # добавляет в экземпляр с заполненными полями в список и возвращает его
            vacancy_instances.append(vacancy)
        return vacancy_instances