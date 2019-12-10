import requests
import csv


def take_friends():
    """Вернуть список друзей."""
    token = '' #Token
    version = 5.103
    fields = 'fields'
    user_id = '53083705'
    response = requests.get('https://api.vk.com/method/friends.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'fields': fields,
                                'user_id': user_id,

                            })
    data = response.json()['response']['items']
    return data


def file_write(friends):
    """Записать данные в файл"""
    with open('user_friends.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('ID', 'Имя', 'Фамилия'))
        for user in friends:
            user_id = user['id']
            first_name = user['first_name']
            last_name = user['last_name']
            a_pen.writerow((user_id, first_name, last_name))


friends = take_friends()
file_write(friends=friends)


def print_friends(take_friends):
    """Напечать друзей пользователя в консоле."""
    for take_friend in take_friends:
        user_id = take_friend['id']
        first_name = take_friend['first_name']
        last_name = take_friend['last_name']
        result = '{} {}, id - {}'.format(first_name, last_name, str(user_id))
        print(result)


take_friends = take_friends()
print_friends(take_friends)
