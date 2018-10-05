import random

import requests
from faker import Faker

from settings import URL_REGISTER, URL_LOGIN, URL_LIKE, HEADERS


def get_random_emails(count):
    fake = Faker()
    domains = ['hotmail.com', 'gmail.com', 'aol.com', 'mail.com', 'mail.kz', 'yahoo.com']
    return [
        '@'.join([(fake.name()).lower().replace(' ', '_'), random.choice(domains)])
        for _ in range(count)
    ]


def register_user(client, email):
    register_data = {
        'email': email,
        'password': email * 2,
        'password_confirmation': email * 2,
    }
    return client.post(URL_REGISTER, data=register_data, headers=HEADERS)


def auth_user(client, email):
    login_data = {
        'email': email,
        'password': email * 2,
    }

    response = client.post(URL_LOGIN, data=login_data, headers=HEADERS)
    return client if response.status_code == 200 else None


def like_participant(client, user_id):
    like_data = {
        'isLike': 1,
        'photoId': user_id,
    }
    response = client.post(URL_LIKE, data=like_data, headers=HEADERS)
    return response.text, response.status_code == 200


def make_magic_like(user_id, count):
    liked_user = []

    for email in get_random_emails(count):
        client = requests.Session()

        response = register_user(client, email)
        if response.status_code == 200:

            body, liked = like_participant(client, user_id)
            if liked:
                liked_user.append(email)

            elif 'req' in response.text:

                # Если пользователь не авторизован
                client = auth_user(client, email)
                if client is not None:

                    _, liked = like_participant(client, user_id)
                    if liked:
                        liked_user.append(email)

    return ', '.join(*liked_user)
