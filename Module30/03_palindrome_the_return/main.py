from collections import deque


def can_be_poly_2(string: str) -> bool:
    my_list = deque(string)
    reversed_list = list(reversed(my_list))
    for i_index in range(len(my_list)):
        if my_list[i_index] != reversed_list[i_index]:
            return False
    return True


def can_be_poly_1(string: str) -> bool:
    if string == string[::-1]:
        return True
    return False


print(can_be_poly_1('abcba'))
print(can_be_poly_1('abbbc'))
print(can_be_poly_2('abcba'))
print(can_be_poly_2('abbbc'))
