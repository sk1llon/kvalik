war_and_peace = open('voyna-i-mir.zip', 'r')
dictionary = dict()
for i_line in war_and_peace:
    if i_line != '\n':
        for i_word in i_line:
            if i_word != ' ':
                if i_word in dictionary:
                    dictionary[i_word] += 1
                else:
                    dictionary[i_word] = 1
war_and_peace.close()
