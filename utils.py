import json

import requests

import magic

from constants import FILE_URL, FILE_NAME_ONLINE

mime = magic.Magic(mime=True)


def get_data(link_data, file_data):

    data_json = ''

    try:
        if requests.get(FILE_URL).status_code == 200:
            print('Загружены данные из сети онлайн\n')
            data_json = requests.get(link_data).json()
            with open('data_online.json', mode='w', encoding='utf-8') as file:
                file.write(requests.get(link_data).text)
    except requests.exceptions.ConnectionError as e:
        print(e, '\n')

    try:
        if mime.from_file(FILE_NAME_ONLINE) == 'text/plain':
            print('Отсутствует доступ к онлайн данным, загружаю последнюю сохраненную версию\n')
            data_json = FILE_NAME_ONLINE
    except Exception as e:
        print(e, '\n')

    if data_json == '':
        print('Отсутствует доступ к ранее сохраненным данным, загружаю тестовый пример данных\n')
        with open(file_data, mode='r', encoding='utf-8') as file:
            data_json = json.load(file)

    return data_json
