from src.vacancy_manager import ManagerJsonVac
import os


def test_save_on(test_class_list):
    ManagerJsonVac.save_on(test_class_list, 'test_json_file.json')
    assert os.path.isfile('test_json_file.json')


def test_show_by():
    bob_list = ManagerJsonVac.show_by('name', 'Lida',  'test_json_file.json')
    assert bob_list[0]['name'] == "Lida"
    assert bob_list[0]['age'] == 30
    assert bob_list[0]['height'] == 158.8
    bob_list = ManagerJsonVac.show_by('age', 14,  'test_json_file.json')
    assert bob_list[0]['name'] == "Eric"
    assert bob_list[0]['age'] == 14
    assert bob_list[0]['height'] == 165.4
    bob_list = ManagerJsonVac.show_by('age', '<18', 'test_json_file.json')
    assert bob_list[0]['age'] == 14
    assert bob_list[1]['age'] == 17
    bob_list = ManagerJsonVac.show_by('age', '>18', 'test_json_file.json')
    assert bob_list[0]['age'] == 27
    assert bob_list[1]['age'] == 30