#!/bin/python3
# находит файлы в папке, с датой в названии
# изменяет формат даты с американского на европейский
import os
import re
import shutil
# регулярка для поиска даты в названиях файлов
datePattern = re.compile(r"""^(.*?) # весь текст перед датой
            ((0|1)?\d)- # одна или две цифры месяца
            ((0|1|2|3)?\d)- # одна или две цифры числа
            ((19|20)\d\d) # четыре цифры года
(.*?)$""", re.VERBOSE)  # весь текст после даты

# организовать цикл по файлам в каталоге поиска
for amerFilename in os.listdir('I:\\test'):
    mo = datePattern.search(amerFilename)
    # пропуск файлов, не содержащих дат в имени
    if mo == None:
        continue

    # получить отдельные фрагменты файлов
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # сформировать имена файлов, соответствующие европейскому стандарту
    euroFulename = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart
    # сформировать абсолютные пути к файлам
    absWorkDir = os.path.abspath('I:\\test')
    amerFilename = os.path.join(absWorkDir, amerFilename)
    euroFulename = os.path.join(absWorkDir, euroFulename)

    # переименовать файлы
    print(f'заменяем имя файла {amerFilename} на {euroFulename}')
    shutil.move(amerFilename, euroFulename)
