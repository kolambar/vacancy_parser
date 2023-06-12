from abc import ABC, abstractmethod
from src.converter import Converter


class Vacancy:
    """
    класс для работы с вакансиями
    """
    __slots__ = ('name', 'place', 'salary_from', 'salary_to', 'salary_currency', 'salary_to_compare', 'url',
                 'description', 'operating_mode', 'made_from')

    def __repr__(self):
        return f'Название: {self.name}, место: {self.place}, зп от: {self.salary_from}, зп до: {self.salary_to},' \
               f'зп для сравнения: {self.salary_to_compare} {self.salary_currency}, ссылка: {self.url}, ' \
               f'описание: {self.description},\nрежим работы: {self.operating_mode}, размещено на {self.made_from}'

    def __gt__(self, other):
        """
        по зарплате
        self > other
        :param other:
        :return:
        """

        # если нет минимальной зарплаты, то приравнивает ее к максимальной.
        if not self.salary_from:
            self.salary_from = self.salary_to
        if not other.salary_from:
            other.salary_from = other.salary_to

        # проверяет, чтобы валюта была в рублях. если нет, через Converter переводит в рубли
        appropriate_currency = ('RUR', 'rub')
        if self.salary_currency not in appropriate_currency:
            self.salary_from = Converter(self.salary_from, self.salary_currency).rub_amount
        if other.salary_currency not in appropriate_currency:
            other.salary_from = Converter(other.salary_from, other.salary_currency).rub_amount

        return self.salary_from > other.salary_from


    def check_data(self):
        """
        валидирует данные
        :return:
        """
        pass


class VacanciesManager(ABC):
    """
    абстрактный класс принуждает иметь методы:
    - добавления вакансий в JSON
    - отабражения вакансий по критериям
    - удаление вакансий
    """

    @abstractmethod
    def save_on(self):
        """
        добавления вакансий в JSON
        :return:
        """
        pass

    @abstractmethod
    def show_by(self):
        """
        отабражения вакансий по критериям
        :return:
        """
        pass

    @abstractmethod
    def del_vacancy(self):
        """
        удаление вакансий
        :return:
        """
        pass


class ManagerJsonVac(VacanciesManager):

    def save_on(self):
        pass

    def show_by(self):
        pass

    def del_vacancy(self):
        pass
