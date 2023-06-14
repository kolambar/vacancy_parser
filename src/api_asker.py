from abc import ABC, abstractmethod
import requests
import os


class ApiAsker(ABC):
    """
    абстрактный клас требующий метод для подключения по API и метод для получения вакансий
    """
    @abstractmethod
    def get_vacancy(self):
        """
        метод для получения вакансий
        :return:
        """
        pass


class HhApiAsker(ApiAsker):
    """
    подключается к HeadHunter
    """
    def get_vacancy(self):
        """
        подключается к HeadHunter и получает вакансии
        """
        return requests.get('https://api.hh.ru/vacancies/?per_page=100').json()


class SjApiAsker(ApiAsker):
    """
    подключается к Superjob
    """
    def get_vacancy(self):
        """
        подключается к Superjob и получает вакансии
        """
        # параметры для superjob
        headers = {'X-Api-App-Id': os.getenv("X-Api-App-Id")}
        params = {
            "count": 100,
            "page": 1,
        }
        return requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers).json()
