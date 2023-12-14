import os
from pathlib import Path
import shutil
import secrets
import string
import time


def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(length))
    return crypt_rand_string

length = 10
shifr = {}



path = input('Введите путь до директории: \n')
path = Path(path)
print(path)

list_dir = os.listdir(path)

for sub_dir in list_dir:
    path_2 = Path(os.path.join(path,sub_dir))
    list_sub_dir = os.listdir(path_2)
    for sub_sub_dir in list_sub_dir:
        path_3 = Path(os.path.join(path_2,sub_sub_dir))
        list_sub_sub_dir = os.listdir(path_3)
        for sub_sub_sub_dir in list_sub_sub_dir:
            path_4 = Path(os.path.join(path_3,sub_sub_sub_dir))
            new_name_folder = generate_alphanum_crypt_string(length)
            new_path = Path(os.path.join(path_3,new_name_folder))
            shifr[sub_sub_sub_dir] = new_name_folder
            print(f"заменяем {sub_sub_sub_dir} на {new_name_folder}")
            os.rename(path_4, new_path)

for k in shifr:
    print(k, ": ", shifr[k])


filename = time.strftime('%Y-%m-%d %H-%M') + '.txt'
with open(filename, 'w', encoding='utf-8') as file:
    for key, value in shifr.items():
        file.write(f'{key} : {value}\n')
