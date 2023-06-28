alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))
new_text = ''
for index in text:
    if index != ' ':
        new_index = alphabet.index(index) + shift
        if new_index > 32:
            new_index -= 33
            memory = alphabet[new_index]
            new_text += memory
        else:
            memory = alphabet[new_index]
            new_text += memory
    else:
        new_text += index
print(new_text)
