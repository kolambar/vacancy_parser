from src.api_asker import HhApiAsker, SjApiAsker


def test_get_vacancy():
    test = HhApiAsker()
    inf = test.get_vacancy()
    assert inf
    assert type(inf) is list

    test = SjApiAsker()
    inf = test.get_vacancy()
    assert inf
    assert type(inf) is list
