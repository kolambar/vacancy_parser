from src.vacancy import Vacancy
from abc import ABC, abstractmethod
from src.converter import Converter


class CreatorOfVacancies(ABC):
    """
    абстрактный класс для приобразования инфы от api в класс Vacancy
    """
    @staticmethod
    @abstractmethod
    def make_vacancy(job: dict):
        """
        функция для приобразования инфы от api в класс Vacancy
        :param job:
        :return list of Vacancy:
        """
        pass

    @staticmethod
    @abstractmethod
    def get_num_to_compare(salary_from: int | None, salary_to: int | None):
        """
        функция для получения из любого сочитания min max зарплат числа для сравнения вакансий по оплате
        :return salary_to_compare:
        """
        pass


class CreatorFromHh(CreatorOfVacancies):

    @staticmethod
    def make_vacancy(job: dict) -> list:
        """
        функция для приобразования инфы от api в класс Vacancy
        :param job:
        :return list of Vacancy:
        """
        vacancy_instances = []  # список для хранения экземпляров
        vacancies = job['items']  # берет только информацию о вакансиях

        for vac in vacancies:

            vacancy = Vacancy()

            # каждую вакансию превращает в объект класса Vacancy, присваивая полям значения из словаря
            vacancy.name = vac['name']   # название вакансии
            vacancy.place = vac['area']['name']   # место работы территориально

            # получает зарплату и на ее основе выводит число для сравнение вакансий по зп (salary_to_compare)
            if vac['salary']:
                vacancy.salary_from = vac['salary']['from']
                vacancy.salary_to = vac['salary']['to']
                vacancy.salary_currency = vac['salary']['currency']
                vacancy.salary_to_compare = CreatorFromHh.get_num_to_compare(vacancy.salary_from, vacancy.salary_to)
            else:
                # этот блок нежен, чтобы у всех вакансий были поля с зп, даже если vac['salary'] = None
                vacancy.salary_from = None
                vacancy.salary_to = None
                vacancy.salary_to_compare = 0
                vacancy.salary_currency = 'rub'

            # если валюта не рубли, то сумму для сравнения переведет в rub, чтобы можно было сортировать по зп
            if vacancy.salary_currency not in ('RUR', 'rub'):
                vacancy.salary_to_compare = Converter(vacancy.salary_to_compare, vacancy.salary_currency).rub_amount

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

    @staticmethod
    def get_num_to_compare(salary_from, salary_to):
        """
        функция для получения из любого сочитания min max зарплат числа для сравнения вакансий по оплате
        :return salary_to_compare:
        """
        if salary_from and salary_to:
            return (salary_from + salary_to) / 2
        elif salary_from:
            return salary_from
        elif salary_to:
            return salary_to
        else:
            return 0


class CreatorFromSj(CreatorOfVacancies):

    @staticmethod
    def make_vacancy(job: dict) -> list:
        """
        функция для приобразования инфы от api в класс Vacancy
        :param job:
        :return list of Vacancy:
        """
        vacancy_instances = []  # список для хранения экземпляров
        vacancies = job['objects']  # берет только информацию о вакансиях

        for vac in vacancies:
            vacancy = Vacancy()

            # каждую вакансию превращает в объект класса Vacancy, присваивая полям значения из словаря
            vacancy.name = vac['profession']   # название вакансии

            # место работы территориально. обработка случаев, когда место не указано
            if vac['payment_from']:
                vacancy.place = vac['address']
            else:
                vacancy.place = 'Возможно место указано в описании или названии работы'

            # получает зарплату и на ее основе выводит число для сравнение вакансий по зп (salary_to_compare)
            vacancy.salary_from = vac['payment_from']
            vacancy.salary_to = vac['payment_to']
            vacancy.salary_currency = vac['currency']
            vacancy.salary_to_compare = CreatorFromSj.get_num_to_compare(vacancy.salary_from, vacancy.salary_to)

            # если валюта не рубли, то сумму для сравнения переведет в rub, чтобы можно было сортировать по зп
            if vacancy.salary_currency not in ('RUR', 'rub'):
                vacancy.salary_to_compare = Converter(vacancy.salary_to_compare, vacancy.salary_currency).rub_amount

            vacancy.url = vac['link']
            vacancy.description = vac['candidat']  # описание работы
            vacancy.operating_mode = vac['type_of_work']['title']

            # оставляет метку, где была взята вакансия
            vacancy.made_from = 'SuperJob'

            # добавляет в экземпляр с заполненными полями в список и возвращает его
            vacancy_instances.append(vacancy)
        return vacancy_instances

    @staticmethod
    def get_num_to_compare(salary_from, salary_to):
        """
        функция для получения из любого сочитания min max зарплат числа для сравнения вакансий по оплате
        :return salary_to_compare:
        """
        if salary_from and salary_to:
            return (salary_from + salary_to) / 2
        elif salary_from:
            return salary_from
        elif salary_to:
            return salary_to
        else:
            return 0
