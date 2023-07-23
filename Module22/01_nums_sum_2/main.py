numbers_file = open('numbers.txt', 'r')
sum_of_numbers = 0
for i_element in numbers_file:
    if i_element != ' ' and i_element != '\n':
        sum_of_numbers += int(i_element)
answer_file = open('answer.txt', 'w')
answer_file.write(str(sum_of_numbers))
numbers_file.close()
answer_file.close()
