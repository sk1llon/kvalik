nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def first_nested_list(main_list):
    def second_nested_list(my_list):
        result = []
        for i_num in my_list:
            if isinstance(i_num, int):
                result.append(i_num)
            else:
                result.extend(second_nested_list(i_num))
        return result
    return second_nested_list(main_list)


print(first_nested_list(nice_list))