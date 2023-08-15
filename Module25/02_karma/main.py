import random


class Buddhist:
    def __init__(self, karma=0):
        self.__karma = karma

    def set_karma(self, karma):
        self.__karma += karma

    def get_karma(self):
        return self.__karma


def one_day(day_count):
    if random.randint(1, 10) == 1:
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            karma = random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            karma_log.write('День {}. Проступок - {}\n'.format(
                day_count, karma
            ))
            return False
    else:
        return random.randint(1, 7)


buddhist = Buddhist()
count = 0
while buddhist.get_karma() < 500:
    count += 1
    if one_day(count):
        pass
    else:
        buddhist.set_karma(one_day(count))
print('Просветление достигнуто!')
