def sum_of_elements(*args):
    def nested_list(my_list):
        result = []
        for i_arg in my_list:
            if isinstance(i_arg, int):
                result.append(i_arg)
            else:
                result.extend(nested_list(i_arg))
        return result
    return sum(nested_list(args))


print(sum_of_elements([[1, 2, [3]], [1], 3]))
print(sum_of_elements(1, 2, 3, 4, 5))
