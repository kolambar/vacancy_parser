from src.vacancy_manager import ManagerJsonVac
import os


data = ManagerJsonVac.open_file('test_json_file.json')

def test_save_on(test_class_list):
    ManagerJsonVac.save_on(test_class_list, 'test_json_file.json')
    assert os.path.isfile('test_json_file.json')


def test_show_by_criterion():
    bob_list = ManagerJsonVac.show_by_criterion('name', 'Lida',  data)
    assert bob_list[0]['name'] == "Lida"
    assert bob_list[0]['age'] == 30
    assert bob_list[0]['height'] == 158.8
    bob_list = ManagerJsonVac.show_by_criterion('age', 14,  data)
    assert bob_list[0]['name'] == "Eric"
    assert bob_list[0]['age'] == 14
    assert bob_list[0]['height'] == 165.4


def test_show_by_salary():
    bob_list = ManagerJsonVac.show_by_salary('age', '<18', data)
    assert bob_list[0]['age'] == 14
    assert bob_list[1]['age'] == 17
    bob_list = ManagerJsonVac.show_by_salary('age', '>18', data)
    assert bob_list[0]['age'] == 27
    assert bob_list[1]['age'] == 30


def test_show_by_key():
    bob_list = ManagerJsonVac.show_by_key('name', 'l',  data)
    assert bob_list[0]['name'] == "Lida"


def test_del_vacancy():
    bob_list = ManagerJsonVac.show_by_salary('age', '<18', data)
    ManagerJsonVac.del_vacancy(bob_list)
    assert bob_list == []
