from src.converter import Converter


def test___init__():
    cost = Converter(3500, 'USD')
    assert cost.rub_amount > 3500
    assert isinstance(cost.rub_amount, float)


def test_situation():
    class Money:
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency

    cost = Money(100, 'EUR')

    cost.amount = Converter(cost.amount, cost.currency).rub_amount

    assert cost.amount > 100
    assert isinstance(cost.amount, float)
