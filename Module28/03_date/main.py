class Date:
    def __init__(self, *args):
        self.day, self.month, self.year = args

    @classmethod
    def parse_date_str(cls, str_date):
        return tuple(map(int, str_date.split('-')))

    @classmethod
    def is_date_valid(cls, str_date):
        day, month, year = cls.parse_date_str(str_date)
        return 0 <= day <= 31 and 0 < month <= 12 and year > 0

    @classmethod
    def from_string(cls, str_date):
        try:
            assert cls.is_date_valid(str_date)
            return cls(*cls.parse_date_str(str_date))
        except AssertionError:
            print('Неправильный формат даты')

    def __str__(self):
        return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(day=self.day,
                                                                 month=self.month,
                                                                 year=self.year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
test = Date.from_string('154-123-542')
print(test)
