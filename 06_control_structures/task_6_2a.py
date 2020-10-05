# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


address = input('Vvedi IP address v formate x.x.x.x: ')

tochki = address.count('.')

if tochki != 3:
    print('TOCHKAMI DELI EZHI BLYA')
else:
    address_list = address.strip().split('.')
    oktet1 = address_list[0].isdigit()
    oktet2 = address_list[1].isdigit()
    oktet3 = address_list[2].isdigit()
    oktet4 = address_list[3].isdigit()
    if oktet1 is not True and oktet2 is not True and oktet3 is not True and oktet4 is not True:
        print('ETO NE CHISLA EBLO')
    else:  
        num1 = int(address_list[0])
        num2 = int(address_list[1])
        num3 = int(address_list[2])
        num4 = int(address_list[3])
        allowed_range = list(range(0,256))
        if num1 not in allowed_range or num2 not in allowed_range or num3 not in allowed_range or num4 not in allowed_range:
            print('CHISLA OT 0 DO 255 GAVNO TUPOE')
        else:
            if int(address_list[0]) in range(1,224):
                print('unicast')
            elif int(address_list[0]) in range(224,240):
                print('multicast')
            elif address == '255.255.255.255':
                print('local broadcast')
            elif address == '0.0.0.0':
                print('unassigned')
            else:
                print('unused')

