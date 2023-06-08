from src.creator_of_vacancies import CreatorFromHh, CreatorFromJs
from src.vacancy import Vacancy


def test_make_vacancy(test_dict_hh):
    test_vacancy_instances = CreatorFromHh.make_vacancy(test_dict_hh)
    assert type(test_vacancy_instances[0]) == Vacancy
    assert test_vacancy_instances[0].operating_mode == 'Полная занятость'
    assert test_vacancy_instances[0].salary_to is None
    assert test_vacancy_instances[0].salary_from == 300000

def test_make_vacancy_js(test_dict_sj):
    test_vacancy_instances = CreatorFromJs.make_vacancy(test_dict_sj)
    assert type(test_vacancy_instances[0]) == Vacancy
    assert test_vacancy_instances[0].url == 'https://himki.superjob.ru/vakansii/zaveduyuschij-kabinetom-mrt-vrach-rentgenolog-39075693.html'
    assert test_vacancy_instances[0].salary_to is None
    assert test_vacancy_instances[0].salary_from == 120000