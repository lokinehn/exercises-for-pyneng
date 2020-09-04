# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1_list = command1.split()[-1].split(',')
command2_list = command2.split()[-1].split(',')
command1_set = set(command1_list)
command2_set = set(command2_list)
vlans = sorted(list(command1_set & command2_set))
print(vlans)
