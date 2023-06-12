from src.vacancy import Vacancy
from src.api_asker import HhApiAsker
from src.creator_of_vacancies import CreatorFromHh


def test___gt__():
    sad = HhApiAsker()
    sad_list = sad.get_vacancy()
    sad_list_of_vac = CreatorFromHh()
    sad_list_of_vac = sad_list_of_vac.make_vacancy(sad_list)
    print(sad_list_of_vac)

