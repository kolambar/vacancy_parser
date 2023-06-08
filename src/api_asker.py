from abc import ABC, abstractmethod
import requests
import os


# параметры для superjob
headers = {'X-Api-App-Id': os.getenv("X-Api-App-Id")}

params = {
    "count": 100,
    "page": 1,
}

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
        return requests.get('https://api.hh.ru/vacancies/?per_page=100').json()


class SuperApiAsker(ApiAsker):
    """
    подключается к Superjob
    """
    def get_vacancy(self):
        return requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=headers).json()

#
# sad = HhApiAsker()
#
# for_print = sad.get_vacancy()
# print(for_print)
