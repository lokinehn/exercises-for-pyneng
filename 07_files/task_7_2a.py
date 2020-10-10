# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]


with open('config_sw1.txt','r') as text:
    config = text.readlines()
    for lines in config:
        if lines[0] == '!':
            continue
        else:
            if lines.find(ignore[0]) is -1 and lines.find(ignore[1]) is -1 and lines.find(ignore[2]) is -1:
                print(lines.rstrip())
            else:
                continue
