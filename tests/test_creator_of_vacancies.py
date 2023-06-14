from src.creator_of_vacancies import CreatorFromHh, CreatorFromSj
from src.vacancy import Vacancy


def test_make_vacancy(test_dict_hh):
    test_vacancy_instances = CreatorFromHh.make_vacancy(test_dict_hh)
    assert type(test_vacancy_instances[0]) == Vacancy
    assert test_vacancy_instances[0].operating_mode == 'Полная занятость'
    assert test_vacancy_instances[0].salary_to is None
    assert test_vacancy_instances[0].salary_from == 300000


def test_make_vacancy_js(test_dict_sj):
    test_vacancy_instances = CreatorFromSj.make_vacancy(test_dict_sj)
    assert type(test_vacancy_instances[0]) == Vacancy
    assert '/zaveduyuschij-kabinetom-mrt-vrach-rentgenolog-39075693.html' in test_vacancy_instances[0].url
    assert test_vacancy_instances[0].salary_to is 0
    assert test_vacancy_instances[0].salary_from == 120000


def test_get_num_to_compare():
    hh_from_none = None
    hh_from_num = 6
    hh_to_none = None
    hh_to_num = 10
    assert CreatorFromHh.get_num_to_compare(hh_from_none, hh_to_num) == 10
    assert CreatorFromHh.get_num_to_compare(hh_from_num, hh_to_num) == 8
    assert CreatorFromHh.get_num_to_compare(hh_from_num, hh_to_none) == 6
    assert CreatorFromHh.get_num_to_compare(hh_from_none, hh_to_none) == 0

    sj_from_nil = 0
    sj_from_num = 6
    sj_to_nil = 0
    sj_to_num = 10
    assert CreatorFromSj.get_num_to_compare(sj_from_nil, sj_to_num) == 10
    assert CreatorFromSj.get_num_to_compare(sj_from_num, sj_to_num) == 8
    assert CreatorFromSj.get_num_to_compare(sj_from_num, sj_to_nil) == 6
    assert CreatorFromSj.get_num_to_compare(sj_from_nil, sj_to_nil) == 0
