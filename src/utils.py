from src.vacancy_manager import ManagerJsonVac


def ask_me(choice):

    solution_methods = {'1': 'new_json_file_hh.json', '2': 'new_json_file_sj.json', '3': 'new_json_file.json'}
    data = ManagerJsonVac.open_file(solution_methods[choice])

    # сортирует по професии
    profession = input('Напишите название профессии, по которой нужно предоставить информацию\n'
                       'Если хотите пропустить, нажмите Enter\n')
    if profession:
        data = ManagerJsonVac.show_by_key("name", profession, data)

    # сортирует по зарплате
    salary = input('Какая зарплата Вас интересует?\n'
          'Напишите "<" или ">" и зарплату в рублях без пробелов.\n'
          'Пример ">20000"\n'
          'Если хотите пропустить, нажмите Enter\n')
    if salary:
        data = ManagerJsonVac.show_by_salary("salary_to_compare", salary, data)

    # сортирует по месту работы
    place = input('Где бы Вы хотели работать?\n'
                  'Напишите название города или региона.\n'
                  'Если хотите пропустить, нажмите Enter\n')
    if place:
        data = ManagerJsonVac.show_by_criterion("place", place, data)

    # сортирует по рабочему режиму
    operating_mode = input('Если вам важен режим работы напишите соответствующее число:\n'
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

    return data
