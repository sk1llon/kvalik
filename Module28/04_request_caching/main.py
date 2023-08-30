import copy


class LRUCache:
    cache_list = list()

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = 0

    @property
    def cache(self):
        if len(self.cache_list) > 0:
            for i_key, i_value in self.cache_list[0].items():
                return 'Самый старый запрос - {i_key}: {i_value}'.format(i_key=i_key,
                                                                         i_value=i_value)
        return 'Список запросов пуст'

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        dictionary = dict()
        if self.current_capacity < self.capacity:
            self.current_capacity += 1
            dictionary[key] = value
            dict_copy = copy.deepcopy(dictionary)
            self.cache_list.append(dict_copy)
            dictionary.clear()
        else:
            self.cache_list.pop(0)
            dictionary[key] = value
            dict_copy = copy.deepcopy(dictionary)
            self.cache_list.append(dict_copy)
            dictionary.clear()

    def print_cache(self):
        for i_index in range(len(self.cache_list)):
            for i_keys, i_values in self.cache_list[i_index].items():
                print(i_keys, ':', i_values)

    def get(self, key):
        for i_index, i_value in enumerate(self.cache_list):
            for i_keys, i_values in i_value.items():
                if i_keys == key:
                    if i_index != len(self.cache_list):
                        self.cache_list[i_index], self.cache_list[i_index + 1] = self.cache_list[i_index + 1],\
                                                                                     self.cache_list[i_index]
                    return i_values


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

print(cache.cache)

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
