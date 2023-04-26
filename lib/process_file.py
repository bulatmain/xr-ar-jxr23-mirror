'''
Finds bestmatching json file by its name for further reading

The output of function get_info_from_file is a python's array of info or idk
'''

from os import path, listdir
from Levenshtein import distance

import json


DEFAULT_FILENAME = 'template.json'


def get_info_from_file(possible_filenames):
    base_path = path.dirname(__file__)
    db_path = path.abspath(path.join(base_path, '..', 'db'))

    min_diff = 1e9
    min_diff_file = ''
    for possible_filename in possible_filenames:
        for current_file in listdir(db_path):
            current_diff = distance(possible_filename, current_file)
            if min_diff > current_diff:
                min_diff = current_diff
                min_diff_file = current_file

        filename = min_diff_file
    
    if min_diff > 3:
        # print('There is no such file, or medicine was not recognized properly.')
        filename = DEFAULT_FILENAME

    filepath = path.join(db_path, filename)

    matched_file = open(filepath, 'r')

    response = {
        # 'Название препарата': '',
        # 'Действующее вещество': '',
        # 'Форма выпуска': '',
        # 'Фармакологическое действие': '',
        # 'Показания к применению': '',
        # 'Противопоказания': '',
        # 'Побочные эффекты': '',
        # 'Способ применения и дозировка': '',
        # 'Особые указания': '',
        # 'Взаимодействие с другими лекарствами': '',
        # 'Условия хранения': '',
        # 'Срок годности': ''
    }

    data = json.loads(matched_file.read())
    for key, value in zip(data.keys(), data.values()):
        response[key] = value

    matched_file.close()

    return response


if __name__ == '__main__':
    s = input('Input a name of fail that needs to be printed: ')
    print(get_info_from_file(s))
