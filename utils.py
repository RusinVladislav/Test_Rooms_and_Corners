import os.path

import requests

import magic

from constants import FILE_URL, FILE_NAME_ONLINE, FILE_EXAMPLE

mime = magic.Magic(mime=True)


def get_data(link_data):
    data_json = ''

    try:
        if requests.get(FILE_URL).status_code == 200:
            print('Used data from the network online\n')
            with open(FILE_NAME_ONLINE, mode='w', encoding='utf-8') as file:
                file.write(requests.get(link_data).text)
            data_json = os.path.join(FILE_NAME_ONLINE)
    except requests.exceptions.ConnectionError as e:
        print(e, '\n')

    try:
        if data_json == '' and mime.from_file(FILE_NAME_ONLINE) == 'text/plain':
            print('No access to online data, a previously saved version of data from the online network is used\n')
            data_json = FILE_NAME_ONLINE
    except Exception as e:
        print(e, '\n')

    if data_json == '':
        print('There is no access to online data and to previously saved data. Used test case data\n')
        data_json = FILE_EXAMPLE

    return os.path.join(data_json)
