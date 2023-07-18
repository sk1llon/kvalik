
def main(my_list):
    if len(my_list) <= 1:
        return my_list
    main_elem = my_list[-1]
    upper_list = []
    lower_list = []
    equal_list = []
    for i_elem in my_list:
        if i_elem < main_elem:
            lower_list.append(i_elem)
        elif i_elem == main_elem:
            equal_list.append(i_elem)
        else:
            upper_list.append(i_elem)
    return main(lower_list) + equal_list + main(upper_list)


print(main([5, 8, 9, 4, 2, 9, 1, 8]))
