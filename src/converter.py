import requests


class Converter:
    """
    Класс для перевода валюты в рубли
    """

    @staticmethod
    def convert_it(amount: int, currency: str) -> float:
        """
        переводит валюту в рубли
        :param amount:
        :param currency:
        :return rub:
        """

        # Обрабатывает случай неправильного кода белорусских рублей
        if currency == 'BYR':
            currency = 'BYN'

        currency = currency.upper()  # название валюты, сокращенное, 3 большие буквы

        # запрос на сайт для перевода валюты в рубли
        url = f'https://api.exchangerate.host/convert?from={currency}&to=RUB&amount={amount}'
        data = requests.get(url).json()

        return data['result']
