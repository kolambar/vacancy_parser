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

    @staticmethod
    @abstractmethod
    def open_file(json_file):
        """
        отабражения вакансий по критериям
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def del_vacancy(data):
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

    @staticmethod
    def open_file(json_file):
        with open(json_file, 'r', encoding='utf=8') as file:
            return json.load(file)


    @staticmethod
    def show_by_salary(slot, value, data):
        """
        отабражения вакансий по критериям

        находить все вакансии больше или меньше value
        используется для зп
        :return list_of_relevant_vac:
        """
        list_of_relevant_vac = []

        # проверка, нужно ли искать конкретное значения или все, что меньше
        if type(value) is str and value[0] == '<':
            value = int(value[1:])
            for vac in data:
                if vac[slot] < value:
                    list_of_relevant_vac.append(vac)

        # проверка, нужно ли искать конкретное значения или все, что больше
        elif type(value) is str and value[0] == '>':
            value = int(value[1:])
            for vac in data:
                if vac[slot] > value:
                    list_of_relevant_vac.append(vac)

        return list_of_relevant_vac

    @staticmethod
    def show_by_criterion(slot, value, data):
        """
        отабражения вакансий по критериям

        ищет по конкретным value

        :return list_of_relevant_vac:
        """
        list_of_relevant_vac = []

        for vac in data:
            if vac[slot] == value:
                list_of_relevant_vac.append(vac)

        return list_of_relevant_vac

    @staticmethod
    def show_by_key(slot, value, data):
        """
        может искать, есть ли ключевое слово
        в каком-нибудь из полей

        :return list_of_relevant_vac:
        """
        list_of_relevant_vac = []

        for vac in data:
            try:
                if value.lower() in vac[slot].lower():
                    list_of_relevant_vac.append(vac)
            except TypeError:
                pass

        return list_of_relevant_vac

    @staticmethod
    def del_vacancy(list_of_relevant_vac):
        """
        удаляет результат сортировок вакансий.
        сбрасывает фильтры
        """
        list_of_relevant_vac.clear()
        return list_of_relevant_vac
