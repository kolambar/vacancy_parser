from abc import ABC, abstractmethod


class ApiAsker(ABC):
    """
    абстрактный клас требующий метод для подключения по API и метод для получения вакансий
    """
    pass

    @abstractmethod
    def get_connect_with_api(self):
        """
        метод для подключения по api
        :return:
        """
        pass

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

    def get_connect_with_api(self):
        pass

    def get_vacancy(self):
        pass


class SberApiAsker(ApiAsker):
    """
    подключается к Superjob
    """

    def get_connect_with_api(self):
        pass

    def get_vacancy(self):
        pass
