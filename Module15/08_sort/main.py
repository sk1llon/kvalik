goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Введите название фрукта: ')
price = int(input('Введите цену фрукта: '))
goods.append([fruit_name, price])
print('Новый ассортимент:', goods)
for i_goods in range(len(goods)):
    goods[i_goods][1] = goods[i_goods][1] + goods[i_goods][1] * 8 / 100
print('Новый ассортимент с увел. ценой:',goods)