# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


from sys import argv

file1 = argv[1]
file2 = argv[2]

with open(file1,'r') as text, open(file2,'a') as text1:
    for lines in text:
        if lines.find(ignore[0]) is -1 and lines.find(ignore[1]) is -1 and lines.find(ignore[1]) is -1 and lines.find(ignore[2]) is -1:
            text1.write(lines)
        else:
            continue

