from src.vacancy import Vacancy
from src.vacancy_manager import ManagerJsonVac
from src.api_asker import HhApiAsker, SjApiAsker
from src.creator_of_vacancies import CreatorFromHh, CreatorFromSj


def main():

    # загружает актуальные вакансии по api
    hh = HhApiAsker()
    sj = SjApiAsker()
    hh_dict = hh.get_vacancy()
    sj_dict = sj.get_vacancy()

    # трансформирует вакансии с hh в экземпляры класса Vacancy
    vacancy_instances = CreatorFromHh.make_vacancy(hh_dict)

    # добавляет вакансии с sj
    vacancy_instances.extend(CreatorFromSj.make_vacancy(sj_dict))

    # сохраняет все вакансии в файл
    ManagerJsonVac.save_on(vacancy_instances, 'new_json_file.json')

if __name__ == '__main__':
    main()
