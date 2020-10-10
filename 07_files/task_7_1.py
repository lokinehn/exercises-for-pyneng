# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""




with open('ospf.txt') as text:
    ospf = text.readlines()
    for lines in ospf:
        lines = lines.strip().split()
        prefix = lines[1]
        metric = lines[2].strip('[]')
        hop = lines[4].strip(',')
        update = lines[5].strip(',')
        intf = lines[6]
        gavno = '''
        Prefix                {0:18}
        AD/Metric             {1:18}
        Next-Hop              {2:18}
        Last update           {3:18}
        Outbound Interface    {4:18}
        '''
        print(gavno.format(prefix,metric,hop,update,intf))

