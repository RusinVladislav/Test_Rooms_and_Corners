import os.path

import requests

import magic

from constants import FILE_URL, FILE_NAME_ONLINE, FILE_EXAMPLE

mime = magic.Magic(mime=True)


def get_data(link_data):

    data_json = ''

    try:
        if requests.get(FILE_URL).status_code == 200:
            print('Загружены данные из сети онлайн\n')
            with open(FILE_NAME_ONLINE, mode='w', encoding='utf-8') as file:
                file.write(requests.get(link_data).text)
            data_json = os.path.join(FILE_NAME_ONLINE)
    except requests.exceptions.ConnectionError as e:
        print(e, '\n')

    try:
        if data_json == '' and mime.from_file(FILE_NAME_ONLINE) == 'text/plain':
            print('Отсутствует доступ к онлайн данным, загружаю последнюю сохраненную версию данных из сети онлайн\n')
            data_json = FILE_NAME_ONLINE
    except Exception as e:
        print(e, '\n')

    if data_json == '':
        print('Отсутствует доступ к ранее сохраненным данным, загружаю тестовый пример данных\n')
        data_json = FILE_EXAMPLE

    return os.path.join(data_json)
