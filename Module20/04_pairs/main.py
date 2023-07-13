import random

original_list = [random.randint(1, 10) for _ in range(10)]
new_list = []
print('Оригинальный список:', original_list)
zip_list = zip(original_list[::2], original_list[1::2])
for i_zip in zip_list:
    new_list.append(i_zip)
print('Новый список:', new_list)

