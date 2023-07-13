def tpl_sort(main_tuple):
    new_list = list(main_tuple)
    for i_list in new_list:
        if not isinstance(i_list, int):
            print('Одно или несколько чисел не являются целыми')
            return main_tuple
        else:
            for index in range(len(new_list)):  # Ну или же просто return sorted(new_list)
                for current in range(len(new_list)):
                    if new_list[current] > new_list[index]:
                        new_list[current], new_list[index] = new_list[index], new_list[current]
            return tuple(new_list)


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
