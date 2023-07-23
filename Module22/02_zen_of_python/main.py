zen_file = open('zen.txt', 'r')
zen_list = []
for i_line in zen_file:
    zen_list.append(i_line)
new_zen_list = zen_list[::-1]
for i_line in new_zen_list:
    print(i_line, end='')
zen_file.close()
