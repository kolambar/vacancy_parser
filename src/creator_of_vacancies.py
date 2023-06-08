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
    def make_vacancy(job: dict):
        vacancy_instances = []
        vacancies = job['items']
        for vac in vacancies:
            vacancy = Vacancy()
            vacancy.name = vac['name']
            vacancy.place = vac['area']['name']
            vacancy.salary_from = vac['salary']['from']
            vacancy.salary_to = vac['salary']['to']
            vacancy.salary_currency = vac['salary']['currency']
            vacancy.url = vac['alternate_url']

            if vac['snippet']['requirement'] == None:
                vac['snippet']['requirement'] = ''
            if vac['snippet']['responsibility'] == None:
                vac['snippet']['responsibility'] = ''

            vacancy.description = vac['snippet']['requirement'] + '\n' + vac['snippet']['responsibility']
            vacancy.operating_mode = vac['employment']['name']
            vacancy.made_from = 'HeadHunter'
            vacancy_instances.append(vacancy)
        return vacancy_instances

