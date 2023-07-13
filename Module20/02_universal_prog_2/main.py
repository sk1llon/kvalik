def crypto(text):
    result = [index for index, value in enumerate(text) if is_prime(index)]
    new_result = [1]
    new_result.extend(result)
    return new_result


def is_prime(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                return False
        else:
            return True

    else:
        return False


def main(str_letter):
    indexes = crypto(str_letter)
    result = []
    for i_index in indexes:
        result.append(str_letter[i_index])
    return result


letter = input('Введите текст: ').split()
letter = ''.join(letter)
print(main(letter))
