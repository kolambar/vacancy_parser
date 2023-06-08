from abc import ABC, abstractmethod
from vacancy import Vacancy


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
        pass
