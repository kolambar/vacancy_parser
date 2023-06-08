from abc import ABC, abstractmethod


class Vacancy:
    """
    класс для работы с вакансиями
    """
    __slots__ = ('name', 'place', 'salary_from', 'salary_to', 'salary_currency', 'url', 'description', 'operating_mode', 'made_from')

    def __repr__(self):
        return f'Название: {self.name}, место: {self.place}, зп от: {self.salary_from}, зп до: {self.salary_to}, {self.salary_currency},' \
               f' ссылка: {self.url}, описание:\n{self.description},\nрежим работы: {self.operating_mode}, размещено на {self.made_from}'

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
