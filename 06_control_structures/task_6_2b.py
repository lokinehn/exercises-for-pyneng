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
status = False

while not status:
    if address.count('.') != 3:
        print('TOCHKAMI DELI EZHI BLYA')
    elif address.strip().split('.')[0].isdigit() is False or address.strip().split('.')[1].isdigit() is False or address.strip().split('.')[2].isdigit() is False or address.strip().split('.')[3].isdigit() is False:
        print('ETO NE CHISLA EBLO')
    elif int(address.strip().split('.')[0]) not in range(0,256) or int(address.strip().split('.')[1]) not in range(0,256) or int(address.strip().split('.')[2]) not in range(0,256) or int(address.strip().split('.')[3]) not in range (0,256):  
        print('CHISLA OT 0 DO 255 GAVNO TUPOE')
    else:
        if int(address.strip().split('.')[0]) in range(1,224):
            print('unicast')
        elif int(address.strip().split('.')[0]) in range(224,240):
            print('multicast')
        elif address == '255.255.255.255':
            print('local broadcast')
        elif address == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
        status = True
        continue
    address = input('OI TUPOI SUKA, VVEDI NORMALNO: ')


