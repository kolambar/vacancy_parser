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
        vacancy_instances = CreatorFromHh.make_vacancy(hh_dict)

        # сохраняет вакансии с hh в файл
        ManagerJsonVac.save_on(vacancy_instances, 'new_json_file_hh.json')

    if choice.strip() in '23':  # проверяет был, ли выбран 2 или 3 вариант
        # загружает актуальные вакансии по api
        sj = SjApiAsker()
        sj_dict = sj.get_vacancy()

        # трансформирует вакансии с sj в экземпляры класса Vacancy
        vacancy_instances = CreatorFromSj.make_vacancy(sj_dict)

        # сохраняет вакансии с sj в файл
        ManagerJsonVac.save_on(vacancy_instances, 'new_json_file_sj.json')


if __name__ == '__main__':
    main()
