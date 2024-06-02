import requests
import json
from datetime import datetime
import re

url = 'https://66095c000f324a9a28832d7e.mockapi.io/users'

# ответ
response = requests.get(url)
users = response.json()

# 1. Находим пользователя с именем "Wilson VonRueden" и выводим его ID
user_wilson = next((user for user in users if user['name'] == 'Wilson VonRueden'), None)

if user_wilson:
    print(f'ID пользователя Wilson VonRueden: {user_wilson['id']}')
else:
    print(f'Пользователь Wilson VonRueden не найден!')

# 2. Находим общее состояние первых 76 пользователей
total_state = sum(float(user['state']) for user in users[:76])
print(f"Общее состояние первых 76 пользователей: {total_state}")

# 3. Создаем нового пользователя с вашим именем и состоянием 1,000,000
new_user = {
    "name": "Artem",
    "state": 1_000_000
}
response = requests.post(url, data=new_user)
if response.status_code == 201:
    print('Пользователь успешно создан!')
else:
    print('Ошибка при создании пользователя!')


# 4. Находим самого старого пользователя и выводим его имя
def get_oldest_user(users):
    try:
        oldest_user = max(users, key=lambda user: datetime.strptime(user['birth'], "%Y-%m-%dT%H:%M:%S.%fZ"))
        return oldest_user['name']
    except ValueError:
        print('Ошибка при парсинге даты рождения пользователя. Пропустим.')
        return None


oldest_user_name = get_oldest_user(users)
if oldest_user_name:
    print(f'Самый старый пользователь: {oldest_user_name}')
else:
    print("Не удалось определить самого старого пользователя.")

# 5. Находим самого бедного пользователя и выводим его имя
poorest_user = min(users, key=lambda user: float(user['state']))
print(f"Самый бедный пользователь: {poorest_user['name']}")


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
    return april_birthdays


april_birthdays_count = count_april_birthdays(users)
print(f"Количество пользователей, родившихся в апреле: {april_birthdays_count}")
