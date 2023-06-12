from src.creator_of_vacancies import CreatorFromHh, CreatorFromSj


def test___gt__(test_dict_hh, test_dict_sj):
    list_of_vac = CreatorFromHh()
    list_of_vac = list_of_vac.make_vacancy(test_dict_hh)
    assert list_of_vac[1] > list_of_vac[0]

    list_of_vac = CreatorFromSj()
    list_of_vac = list_of_vac.make_vacancy(test_dict_sj)
    assert list_of_vac[0] > list_of_vac[1]
