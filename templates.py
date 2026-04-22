def build_message(data):
    return f"""
Здравствуйте.

Пользователь: {data['username']}
ID: {data['id']}
Ссылка: {data['link']}

Прошу проверить данный аккаунт.

Спасибо.
"""
