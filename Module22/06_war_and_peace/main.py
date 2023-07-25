import zipfile


def unzip(arch):
    zfile = zipfile.ZipFile(arch, 'r')
    for i_name in zfile.namelist():
        zfile.extract(i_name)
    zfile.close()


unzip('voyna-i-mir.zip')
dictionary = dict()
war_and_peace = open('voyna-i-mir.txt', 'r', encoding='utf-8')
for i_line in war_and_peace:
    if i_line != '\n':
        for i_sym in i_line:
            if i_sym != ' ' and i_sym != '\n':
                if i_sym in dictionary:
                    dictionary[i_sym] += 1
                else:
                    dictionary[i_sym] = 1
sorted_dictionary = sorted(dictionary.items(), key=lambda item: item[1])
for index in range(len(sorted_dictionary)):
    print(sorted_dictionary[index][0], sorted_dictionary[index][1])
