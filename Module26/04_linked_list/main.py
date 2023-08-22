class LinkedList:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, *args):
        self.__length = len(args)
        self.__head = self.__Node(args[0]) if self.__length > 0 else None
        self.__tail = self.__head
        for i_index in range(1, self.__length):
            self.__tail.next = self.__Node(args[i_index])
            self.__tail = self.__tail.next

    def __str__(self):
        return '[{list}]'.format(
            list=' '.join(str(i_elem) for i_elem in self
                          )
        )

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self.__length

    def append(self, number):
        if self.__length > 0:
            self.__tail.next = self.__Node(number)
            self.__tail = self.__tail.next
        else:
            self.__head = self.__tail = self.__Node(number)
        self.__length += 1

    def get(self, index):
        self.is_index(index)
        current = self.__head
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, index):
        self.is_index(index)
        if self.__length == 1:
            self.__head = self.__tail = None
        elif index == 0:
            self.__head = self.__head.next
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if index == self.__length - 1:
                self.__tail = current
        self.__length -= 1

    def is_index(self, index):
        if not 0 <= index < self.__length:
            raise IndexError


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
