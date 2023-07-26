with open('people.txt', 'r', encoding='utf-8') as peoples_file:
    sym_count = 0
    try:
        for index, i_line in enumerate(peoples_file):
            clear_line = i_line.rstrip()
            try:
                sym_count += len(clear_line)
                if len(clear_line) < 3:
                    raise ValueError
            except ValueError:
                print('В строке {} менее трёх символов'.format(index + 1))
    finally:
        print('Общее количество символов:', sym_count)



