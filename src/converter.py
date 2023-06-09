import requests

class Converter:
    """
    Класс для перевода валюты в рубли
    """

    __slots__ = ('amount', 'currency', 'rub_amount')
    def __init__(self, amount: str, currency: int) -> None:
        self.amount = amount  # количество денег в иностранной валюте

        # Обрабатывает случай неправильного кода белорусских рублей
        if currency == 'BYR':
            currency = 'BYN'
        self.currency = currency.upper()  # название валюты, сокращенное, 3 буквы

        # запрос на сайт для перевода валюты в рубли
        url = f'https://api.exchangerate.host/convert?from={self.currency}&to=RUB&amount={self.amount}'
        response = requests.get(url)
        data = response.json()
        self.rub_amount = data['result']  # результат - количество рублей

    def __str__(self):
        return f'{self.rub_amount}'
