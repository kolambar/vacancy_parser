class Vacancy:
    """
    класс для работы с вакансиями
    """
    __slots__ = ('name', 'place', 'salary_from', 'salary_to', 'salary_currency', 'salary_to_compare', 'url',
                 'description', 'operating_mode', 'made_from')

    def __repr__(self):
        return f'Название: {self.name}, место: {self.place}, зп от: {self.salary_from}, зп до: {self.salary_to},' \
               f'зп для сравнения: {self.salary_to_compare} {self.salary_currency}, ссылка: {self.url}, ' \
               f'описание: {self.description},\nрежим работы: {self.operating_mode}, размещено на {self.made_from}'

    def __gt__(self, other):
        """
        по зарплате
        self > other
        :param other:
        :return:
        """
        return self.salary_to_compare > other.salary_to_compare

    def __lt__(self, other):
        return self.salary_to_compare < other.salary_to_compare

    # lt eq sorted(list)