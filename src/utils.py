from src.vacancy_manager import ManagerJsonVac
import json
import sys


def ran_out_of_vacancy(data):
    """
    функция следит, чтобы не закончились вакансии и, если это произошло, завершает работу программы
    :param data:
    :return:
    """
    if len(data) == 0:
        sys.exit('К сожалению, подходящих вакансий нет.')
    else:
        print(f'Осталось {len(data)} вакансий')


def ask_me(choice):
    """
    функция общается с пользователем и сортирует вакансии
    :param choice:
    :return data:
    """

    solution_methods = {'1': 'new_json_file_hh.json', '2': 'new_json_file_sj.json', '3': 'new_json_file.json'}
    data = ManagerJsonVac.open_file(solution_methods[choice])

    # сортирует по зарплате
    salary = input('\nКакая зарплата Вас интересует?\n'
                   'Напишите "<" или ">" и зарплату в рублях без пробелов.\n'
                   'Пример ">20000"\n'
                   'Если хотите пропустить, нажмите Enter\n')
    if salary:
        data = ManagerJsonVac.show_by_salary("salary_to_compare", salary, data)
        ran_out_of_vacancy(data)

    # сортирует по месту работы
    place = input('\nГде бы Вы хотели работать?\n'
                  'Напишите название города или региона.\n'
                  'Если хотите пропустить, нажмите Enter\n')
    if place:
        data = ManagerJsonVac.show_by_key("place", place, data)
        ran_out_of_vacancy(data)

    # сортирует по рабочему режиму
    operating_mode = input('\nЕсли вам важен режим работы напишите соответствующее число:\n'
                           '1. Полная занятость\n'
                           '2. Сменный график работы\n'
                           '3. Частичная занятость\n'
                           '4. Работа вахтовым методом\n'
                           '5. Стажировка\n'
                           '6. Проектная работа\n'
                           'Если хотите пропустить, нажмите Enter\n')
    if operating_mode:
        chosen_operating_mode = {
            '1': 'Полная занятость',
            '2': 'Сменный график работы',
            '3': 'Частичная занятость',
            '4': 'Работа вахтовым методом',
            '5': 'Стажировка',
            '6': 'Проектная работа'
        }
        data = ManagerJsonVac.show_by_criterion("operating_mode", chosen_operating_mode[operating_mode], data)
        ran_out_of_vacancy(data)

    return data


def save_result(list_of_relevant_vac, file_with_vac):
    """
    сохраняет результаты подбора в файл.
    перезаписывает содержимое
    :param list_of_relevant_vac:
    :param file_with_vac:
    """
    with open(file_with_vac, 'w', encoding='utf=8') as file:
        json.dump(list_of_relevant_vac, file, indent=2, ensure_ascii=False)


def do_sort(data):
    """
    Спрашивает у пользователя разрешение
    Сортирует список с ЭК
    :param data:
    :return data:
    """
    answer = input('\nОтсортировать вакансии по зарплате?\n'
                   'Напишите "1", если хотите по возрастанию\n'
                   'Напишите "2", если хотите по убыванию\n'
                   'Если хотите пропустить, нажмите Enter\n').strip()

    if answer == '1':
        data = sorted(data)
    elif answer == '2':
        data = sorted(data, reverse=False)
    return data
