nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [index_in_in for index in nice_list for index_in_index in index for index_in_in in index_in_index]
print(new_list)
