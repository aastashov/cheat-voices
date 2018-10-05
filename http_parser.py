import requests
from bs4 import BeautifulSoup

import settings


def get_rating(f_name=None, f_count=None):
    response = requests.get(settings.URL_VOTES)
    if response.status_code != 200:
        return response.text

    result = {}

    soup = BeautifulSoup(response.text)
    users_blocks = soup.findAll('div', {'class': 'votes-item_title'})
    for item in users_blocks:
        _id = item.findAll('div', {'class': 'item_title__like'})[0].attrs['data-id']
        name = item.findAll('h4', {'class': 'item_title__name'})[0].string
        rating = int(item.findAll('span', {'class': 'rating'})[0].string)
        result[f'{name} id: {_id}'] = rating

    sorted_by_value = sorted(result.items(), key=lambda kv: kv[1], reverse=True)

    if f_name is None:
        return '\n'.join([f'{i[1]} - {i[0]}' for i in sorted_by_value if i[1] > 1])

    if f_name == 'all':
        return '\n'.join([f'{i[1]} - {i[0]}' for i in sorted_by_value])

    if f_name == 'top':
        return '\n'.join([f'{i[1]} - {i[0]}' for i in sorted_by_value][:f_count])
