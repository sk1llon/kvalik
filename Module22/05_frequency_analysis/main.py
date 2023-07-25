text_file = open('text.txt', 'w')
text_file.write('Mama myla ramu'.lower())
text_file.close()
analysis = open('analysis.txt', 'a')
text_file = open('text.txt', 'r')
dictionary = dict()
length_of_text = 0
for i_line in text_file:
    if i_line != '\n':
        for i_sym in i_line:
            if i_sym != ' ':
                length_of_text += 1
                if i_sym in dictionary:
                    dictionary[i_sym] += 1
                else:
                    dictionary[i_sym] = 1
sorted_dictionary = sorted(dictionary.items(), key=lambda item: item[1])
for index in range(len(sorted_dictionary)):
    result = str(sorted_dictionary[index][0]) + ' ' + str(round(sorted_dictionary[index][1] / length_of_text, 3))
    result += '\n'
    analysis.write(result)
text_file.close()
analysis.close()
