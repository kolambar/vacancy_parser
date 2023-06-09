from src.converter import Converter


def test___init__():
    cost = Converter(3500, 'USD')
    assert cost.rub_amount > 3500
    assert isinstance(cost.rub_amount, float)
