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
    def show_by(slot, value, json_file):
        """
        отабражения вакансий по критериям
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def del_vacancy():
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
    def show_by(slot, value, json_file):
        """
        отабражения вакансий по критериям

        ищет по конкретным value

        поддерживает возможность находить
        все вакансии больше или меньше value

        может искать, есть ли ключевое слово
         в каком-нибудь из полей
        :return:
        """
        with open(json_file, 'r', encoding='utf=8') as file:
            list_of_relevant_vac = []
            data = json.load(file)

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

            # для остальных случаев
            else:
                for vac in data:
                    if vac[slot] == value:
                        list_of_relevant_vac.append(vac)
                    # чтобы в поиске отображались те вакансии в которых есть ключевое слово
                    elif type(value) == str:
                        try:
                            if value.lower() in vac[slot].lower():
                                list_of_relevant_vac.append(vac)
                        except:
                            pass

        return list_of_relevant_vac


    @staticmethod
    def del_vacancy():
        pass
