# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf1 = ospf_route.split()
prefix = ospf1[0]
admetric = ospf1[1].strip('[]')
hop = ospf1[3].strip(',')
last_up = ospf1[4].strip(',')
out_if = ospf1[5]

template = '''
Prefix                {:<}
AD/Metric             {:<}
Next-Hop              {:<}
Last update           {:<}
Outbound Interface    {:<}
'''

print(template.format(prefix, admetric, hop, last_up, out_if))


