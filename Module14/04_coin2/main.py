def main(x,y,r):
    if abs(x) > r or abs(y) > r:
        print('Монетки в области нет!')
    else:
        print('Монетка где-то рядом!')
x = float(input('Введите x координату: '))
y = float(input('Введите y координату: '))
radius = int(input('Введите радиус: '))
main(x,y,radius)