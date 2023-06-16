from abc import ABC, abstractmethod
import requests
import os


class ApiAsker(ABC):
    """
    абстрактный клас требующий метод для подключения по API и метод для получения вакансий
    """
    @abstractmethod
    def get_vacancy(self, profession):
        """
        метод для получения вакансий
        :return:
        """
        pass


class HhApiAsker(ApiAsker):
    """
    подключается к HeadHunter
    """
    def get_vacancy(self, profession):
        """
        подключается к HeadHunter и получает вакансии
        """
        params = {
            "per_page=100": 100,
            "page": 1,
            "text": profession
        }
        return requests.get('https://api.hh.ru/vacancies/', params=params).json()


class SjApiAsker(ApiAsker):
    """
    подключается к Superjob
    """
    def get_vacancy(self, profession):
        """
        подключается к Superjob и получает вакансии
        """
        # параметры для superjob
        headers = {'X-Api-App-Id': os.getenv("X-Api-App-Id")}
        params = {
            "count": 100,
            "page": 1,
            "keyword": profession
        }
        return requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers).json()
