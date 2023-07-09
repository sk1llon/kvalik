array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
intersection = []
unique = []
for i_el in array_1:
    if i_el in array_3 and i_el in array_2:
        intersection.append(i_el)
print(intersection)
print(sorted(set(array_1).intersection(set(array_2), set(array_3))))

for elem in array_1:
    if elem not in array_2 and elem not in array_3:
        unique.append(elem)
print(unique)
print(sorted(set(array_1) - set(array_2) - set(array_3)))
