def people_dictionary(dct):
    for i_line in first_tour:
        if i_line != '\n':
            new_line = i_line.split()
            dictionary[new_line[0], new_line[1]] = new_line[2]


def second_tour_write(sec_tour, dct):
    for keys, values in dct.items():
        if int(values) > points:
            name_and_surname = keys[1][0] + '. ' + keys[0] + ' ' + values + '\n'
            sec_tour.write(name_and_surname)
    return sec_tour


def amount_of_people_in_second_tour():
    sec_tour = open('second_tour.txt', 'r')
    count = 0
    for i_line in sec_tour:
        if i_line != '\n':
            count += 1
    return count


first_tour = open('first_tour.txt', 'r')
second_tour = open('second_tour.txt', 'a')
points = int(first_tour.read(2))
dictionary = dict()
people_dictionary(dictionary)
second_tour = second_tour_write(second_tour, dictionary)
amount_of_first_tour_winners = amount_of_people_in_second_tour()
print('Содержимое файла second_tour.txt:\n', amount_of_first_tour_winners)
second_tour.read()
first_tour.close()
second_tour.close()
