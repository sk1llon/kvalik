ip_address = input('Введите IP: ').split('.')
test = False
for i_ip in ip_address:
    if len(ip_address) < 4:
        print('Адрес - это четыре числа, разделённые точками')
        test = True
        break
    elif not i_ip.isdigit():
        print(i_ip, ' - это не целое число')
        test = True
        break
    elif not 0 <= int(i_ip) <= 255:
        print('Число находится вне диапазона')
        test = True
        break
if test:
    ip_address = ''
else:
    print('IP-адрес корректен')