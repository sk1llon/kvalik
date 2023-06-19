list = [3070,2060,3090,3070,3090]
max = 0
new_list = []
for a in list:
    if a > max:
        max = a
for b in list:
    if b != max:
        new_list.append(b)
print(new_list)

