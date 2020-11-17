# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    tuple1 = tuple()
    access = {}
    trunk = {}
    with open(config_filename, 'r') as f:
        interface = ''
        for line in f:
            if line.find('FastEthernet') != -1:
                interface = line.split()[-1]
                line = f.readline()
                if line.find('mode access') != -1:
                    line = f.readline()
                    access_vlan = line.split()[-1]
                    if access_vlan.isdigit():
                        access[interface] = int(access_vlan)
                    else:
                        access[interface] = 1
                elif line.find('encapsulation dot1q') != -1:
                    line = f.readline()
                    trunk_vlans = line.split()[-1]
                    trunk_vlans = [int(num) for num in trunk_vlans.split(',')]
                    trunk[interface] = trunk_vlans
                else:
                    pass
    tuple1 = (access, trunk)
    return(tuple1)

