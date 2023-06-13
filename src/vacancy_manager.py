from abc import ABC, abstractmethod
import json


class VacanciesManager(ABC):
    """
    абстрактный класс принуждает иметь методы:
    - добавления вакансий в JSON
    - отабражения вакансий по критериям
    - удаление вакансий
    """

    @staticmethod
    @abstractmethod
    def save_on(instance, json_file):
        """
        добавления вакансий в файл
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

    @staticmethod
    def save_on(vacancy_instances, json_file):
        """
        добавления вакансий в json файл
        :return:
        """
        with open(json_file, 'w', encoding='utf=8') as file:
            list_with_vac = []
            for instance in vacancy_instances:
                dict_of_instance = {slot: getattr(instance, slot) for slot in instance.__slots__}
                list_with_vac.append(dict_of_instance)
            json.dump(list_with_vac, file, indent=2, ensure_ascii=False)

    def show_by(self):
        pass

    def del_vacancy(self):
        pass
