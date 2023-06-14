from src.utils import ask_me
from src.vacancy import Vacancy
from src.vacancy_manager import ManagerJsonVac
from src.api_asker import HhApiAsker, SjApiAsker
from src.creator_of_vacancies import CreatorFromHh, CreatorFromSj


def main():

    choice = input('Здравствуйте!\n'
          'На каких сайтах хотите искать?\n'
          '1. HeadHunter\n'
          '2. SuperJob\n'
          '3. На обоих сайтах\n'
          'Напишите цифру варианта.\n')

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
        ManagerJsonVac.save_on(vacancy_instances_hh, 'new_json_file_hh.json')
        file_with_vac = 'new_json_file_hh.json'
    elif choice.strip() == '2':
        # сохраняет вакансии с sj в файл
        ManagerJsonVac.save_on(vacancy_instances_sj, 'new_json_file_sj.json')
        file_with_vac = 'new_json_file_sj.json'
    elif choice.strip() == '3':
        vacancy_instances_hh.extend(vacancy_instances_sj)
        ManagerJsonVac.save_on(vacancy_instances_hh, 'new_json_file.json')
        file_with_vac = 'new_json_file.json'

    # Обсуждает с пользователем, какую работу тот ищет
    list_of_relevant_vac = ask_me(choice)

    final_decision = input(f'Вывести подходящие вакансии в консоль или записать их в {file_with_vac}\n'
                           f'напишите "1" или "2"').strip(' "')

    if final_decision == '1':
        print(list_of_relevant_vac)
    elif final_decision == '2':
        ManagerJsonVac.save_on(list_of_relevant_vac, file_with_vac)


if __name__ == '__main__':
    main()
