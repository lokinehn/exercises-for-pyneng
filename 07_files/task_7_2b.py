# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]


with open('config_sw1.txt','r') as text, open('config_sw1_cleared.txt','w') as text1:
    config = text.readlines()
    for lines in config:
        if lines.find(ignore[0]) is -1 and lines.find(ignore[1]) is -1 and lines.find(ignore[2]):
            text1.write(lines)
        else:
            continue

