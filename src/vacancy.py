from abc import ABC, abstractmethod


class Vacancy:
    """
    класс для работы с вакансиями
    """
    def __init__(self):
        pass

    def __gt__(self, other):
        """
        по зарплате
        self > other
        :param other:
        :return:
        """
        pass

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
