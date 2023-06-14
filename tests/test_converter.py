from src.converter import Converter


def test_convert_it():
    cost = Converter.convert_it(3500, 'USD')
    assert cost > 3500
    assert isinstance(cost, float)


def test_situation():
    class Money:
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency

    cost = Money(100, 'EUR')
    cost.amount = Converter.convert_it(cost.amount, cost.currency)

    assert cost.amount > 100
    assert isinstance(cost.amount, float)
