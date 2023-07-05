file_name = input('Введите название файла: ')
if file_name.startswith('@' or '№' or '$' or '%' or '^' or '&' or "\ " or '*' or '(' or ')'):
    print('Название начинается на один из специальных символов!')
elif not file_name.endswith('.txt' or '.docx'):
    print('Неверное расширение файла!')
else:
    print('Файл назван верно.')