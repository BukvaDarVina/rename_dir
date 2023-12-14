#!/bin/python3
# найти папки с большим количеством файлов , и папки с самым большим размером гб
import os
from pathlib import Path
path = input('введи дерикторию для поиска:')
path = Path(path)
files = 0
folder = ''
size_mb_big = 0
folder_size_mb = ''
# пройти по дереву каталогов
for foldername, subfolers, filenames in os.walk(path):
    # выводим информацию о каталоге
    print(
        f"-папка - {foldername},содержится подпапок {len(subfolers)}, содержится файлов {len(filenames)}")
    # определяем папку с наибольшим количеством файлов
    if len(filenames) > files:
        files = len(filenames)
        folder = foldername
    total_size = 0
    size_mb = 0
    # определяем наибольшую по размеру папку
    for file in filenames:
        size_mb = round(
            ((os.path.getsize((os.path.join(foldername, file))))/1024)/1024, 2)
        total_size += size_mb
        print(f"---{file}, {size_mb} Мб.")
    if total_size > size_mb_big:
        size_mb_big = total_size
        folder_size_mb = foldername
    print(f"размер папки {foldername} = {round((total_size),2)} Мб.")
    print('')
# выводим папку с наибольшим количеством папок
print(f"больше всего файлов {files}, в папке {folder}".rjust(14))
# выводим папку с наибольшим размером
print(
    f"самая большая папка по размеру {folder_size_mb}, в ней {size_mb_big} Мб.")
