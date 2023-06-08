from src.api_asker import HhApiAsker, SuperApiAsker


def test_get_vacancy():
    test = HhApiAsker()
    inf = test.get_vacancy()
    assert inf
    assert type(inf) is list

    test = SuperApiAsker()
    inf = test.get_vacancy()
    assert inf
    assert type(inf) is list
