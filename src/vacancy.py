class Vacancy:
    """
    класс для работы с вакансиями
    """
    __slots__ = ('name', 'place', 'salary_from', 'salary_to', 'salary_currency', 'salary_to_compare', 'url',
                 'description', 'operating_mode')

    def __init__(self, name=None, place=None, salary_from=None, salary_to=None, salary_currency=None, url=None,
                 description=None, operating_mode=None):
        self.name = name
        self.place = place
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.url = url
        self.description = description
        self.operating_mode = operating_mode

    def __repr__(self):
        return f'Название: {self.name}, место: {self.place}, зп от: {self.salary_from}, зп до: {self.salary_to},' \
               f'зп для сравнения: {self.salary_to_compare} {self.salary_currency}, ссылка: {self.url}, ' \
               f'описание: {self.description},\nрежим работы: {self.operating_mode}'

    def __str__(self):
        return f'\nНазвание: {self.name}\nМесто: {self.place}\nЗарплата от: {self.salary_from}\n' \
               f'Зарплата до: {self.salary_to} {self.salary_currency}\nСсылка: {self.url}\n' \
               f'Описание: {self.description}\nРежим работы: {self.operating_mode}\n'

    def __gt__(self, other):
        """
        по зарплате
        self > other
        :param other:
        :return:
        """
        return self.salary_to_compare > other.salary_to_compare

    def __lt__(self, other):
        """
        по зарплате
        self < other
        :param other:
        :return:
        """
        return self.salary_to_compare < other.salary_to_compare
