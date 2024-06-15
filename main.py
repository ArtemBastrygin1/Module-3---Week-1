import requests
from datetime import datetime
import re


# 1. Находим пользователя с именем "Wilson VonRueden" и выводим его ID

def find_wilson(users):
    user_wilson = next((user for user in users if user['name'] == 'Wilson VonRueden'), None)
    if user_wilson:
        return f'ID пользователя Wilson VonRueden: {user_wilson['id']}'
    else:
        return 'Пользователь Wilson VonRueden не найден!'


# 2. Находим общее состояние первых 76 пользователей

def total_condition(users):
    total_state = sum(float(user['state']) for user in users[:76])
    return f'Общее состояние первых 76 пользователей: {total_state}'


# 3. Создаем нового пользователя с вашим именем и состоянием 1,000,000

def create_user(new_user):
    response_user = requests.post(url, data=new_user)
    if response_user.status_code == 201:
        return 'Пользователь успешно создан!'
    else:
        return 'Ошибка при создании пользователя!'


# 4. Находим самого старого пользователя и выводим его имя

def get_oldest_user(users):
    try:
        oldest_user = max(users, key=lambda user: datetime.strptime(user['birth'], "%Y-%m-%dT%H:%M:%S.%fZ"))
        return f'Самый старый пользователь: {oldest_user['name']}'
    except ValueError:
        return f'Ошибка при парсинге даты рождения пользователя. Пропустим.'


# 5. Находим самого бедного пользователя и выводим его имя

def get_poorest_user(users):
    poorest_user = min(users, key=lambda user: float(user['state']))
    return f'Самый бедный пользователь: {poorest_user['name']}'


# 6. Подсчитываем количество пользователей, родившихся в апреле

def count_april_birthdays(users):
    april_birthdays = 0
    for user in users:
        try:
            birth_month = int(re.search(r"-(\d{2})-", user['birth']).group(1))
            if birth_month == 4:
                april_birthdays += 1
        except (ValueError, AttributeError):
            print(f"Ошибка при парсинге даты рождения пользователя: {user['birth']}. Пропустим.")
    return f'Количество пользователей, родившихся в апреле: {april_birthdays}'


if __name__ == '__main__':
    url = 'https://66095c000f324a9a28832d7e.mockapi.io/users'
    response = requests.get(url)
    users = response.json()
    print(find_wilson(users))

    print(total_condition(users))

    print(create_user(new_user={
        "name": "Artem",
        "state": 1_000_000
    }))
    print(get_poorest_user(users))

    print(count_april_birthdays(users))
