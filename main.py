import sys
from src.vacancy import Vacancy
from src.vacancy_manager import ManagerJsonVac
from src.api_asker import HhApiAsker, SjApiAsker
from src.utils import ask_me, save_result, do_sort
from src.creator_of_vacancies import CreatorFromHh, CreatorFromSj


def main():

    # спрашивает, где искать вакансии
    choice = input('\nЗдравствуйте!\n'
                   'На каких сайтах хотите искать?\n'
                   '1. HeadHunter\n'
                   '2. SuperJob\n'
                   '3. На обоих сайтах\n'
                   'Напишите цифру варианта.\n').strip()
    print('Сбор вакансий может занять около 10 секунд...')

    if choice.strip() in '13':  # проверяет был, ли выбран 1 или 3 вариант
        # загружает актуальные вакансии по api
        hh = HhApiAsker()
        hh_dict = hh.get_vacancy()

        # трансформирует вакансии с hh в экземпляры класса Vacancy
        vacancy_instances_hh = CreatorFromHh.make_vacancy(hh_dict)

    if choice.strip() in '23':  # проверяет был, ли выбран 2 или 3 вариант
        # загружает актуальные вакансии по api
        sj = SjApiAsker()
        sj_dict = sj.get_vacancy()

        # трансформирует вакансии с sj в экземпляры класса Vacancy
        vacancy_instances_sj = CreatorFromSj.make_vacancy(sj_dict)

    if choice.strip() == '1':
        # сохраняет вакансии с hh в файл
        vacancy_instances_hh = do_sort(vacancy_instances_hh)
        ManagerJsonVac.save_on(vacancy_instances_hh, 'new_json_file_hh.json')
        file_with_vac = 'new_json_file_hh.json'
    elif choice.strip() == '2':
        # сохраняет вакансии с sj в файл
        vacancy_instances_sj = do_sort(vacancy_instances_sj)
        ManagerJsonVac.save_on(vacancy_instances_sj, 'new_json_file_sj.json')
        file_with_vac = 'new_json_file_sj.json'
    elif choice.strip() == '3':
        vacancy_instances_hh.extend(vacancy_instances_sj)
        vacancy_instances_hh = do_sort(vacancy_instances_hh)
        ManagerJsonVac.save_on(vacancy_instances_hh, 'new_json_file.json')
        file_with_vac = 'new_json_file.json'
    else:
        sys.exit('Место поиска вакансий выбрано некорректно')

    # Обсуждает с пользователем, какую работу тот ищет
    list_of_relevant_vac = ask_me(choice)

    # Предлогает выбор: вывести вакансии в консоль или оставить их в файле
    final_decision = input(f'\nВывести подходящие вакансии в консоль или записать их в {file_with_vac}\n'
                           f'напишите "1" или "2"\n').strip(' "')

    if final_decision == '1':
        for vac in list_of_relevant_vac:
            print(Vacancy(vac['name'], vac['place'], vac['salary_from'], vac['salary_to'], vac['salary_currency'],
                          vac['url'], vac['description'], vac['operating_mode']))
    elif final_decision == '2':
        save_result(list_of_relevant_vac, file_with_vac)


if __name__ == '__main__':
    main()
