import re


numbers_list = ['9999999999', '999999-999', '99999x9999']
for index in range(len(numbers_list)):
    result = re.findall(r'\b[8,9]\d{9}', numbers_list[index])
    print('{index}-й номер: {value}'.format(index=index + 1,
                                            value=('всё в порядке' if result else 'не подходит')))