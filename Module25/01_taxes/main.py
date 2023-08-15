class Property:
    __worth = 0

    def __init__(self, worth):
        __worth = self.set_worth(worth)

    def set_worth(self, worth):
        if worth > 0:
            self.__worth = worth
        else:
            raise ValueError('Число должно быть больше нуля')

    def get_worth(self):
        return self.__worth

    def tax(self):
        return self.__worth


class Apartment(Property):
    name = 'Квартира'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.get_worth() / 1000


class Car(Property):
    name = 'Машина'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.get_worth() / 200


class CountryHouse(Property):
    name = 'Дача'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.get_worth() / 500


print('------------'
      'Программа для рассчёта налога'
      '------------')
sum_of_tax = 0
amount_of_money = int(input('Сколько у вас денег? '))
aps_worth = int(input('Введите цену квартиры: '))
car_worth = int(input('Введите цену машины: '))
ch_worth = int(input('Введите цену дачи: '))
tax_list = [Apartment(aps_worth), Car(car_worth), CountryHouse(ch_worth)]
for i_element in tax_list:
    print('Налог на {} составляет {} рублей'.format(
        i_element.name, i_element.tax()
    ))
    sum_of_tax += i_element.tax()
print('Общая сумма налога составляет {} рублей'.format(
    sum_of_tax
))
if sum_of_tax > amount_of_money:
    print('К сожалению у вас не хватает {} рублей для оплаты налогов'.format(
        sum_of_tax - amount_of_money
    ))
else:
    print('Налоги успешно оплачены, у вас осталось {} рублей'.format(
        amount_of_money - sum_of_tax
    ))

