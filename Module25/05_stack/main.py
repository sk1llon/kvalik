class Stack:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(', '.join(self.__list))

    def add(self, elem):
        self.__list.append(elem)

    def pop(self):
        if len(self.__list) == 0:
            return None
        return self.__list.pop()


class TaskManager:
    def __init__(self):
        self.dictionary = {}

    def __str__(self):
        string = ''
        for elem in sorted(self.dictionary.keys()):
            string += str(elem) + ' ' + str(self.dictionary[elem]) + ';\n'
        return string

    def new_dict(self, task, priority):
        if priority not in self.dictionary.keys():
            self.dictionary[priority] = Stack()
            self.dictionary[priority].add(task)
        else:
            new_stack = Stack()
            while len(str(self.dictionary[priority])) != 0:
                value = self.dictionary[priority].pop()
                if value != task:
                    new_stack.add(value)
            new_stack.add(task)
            self.dictionary[priority] = new_stack


manager = TaskManager()
manager.new_dict("сделать уборку", 4)
manager.new_dict("помыть посуду", 4)
manager.new_dict("отдохнуть", 1)
manager.new_dict("поесть", 2)
manager.new_dict("сдать дз", 2)
print(manager)
