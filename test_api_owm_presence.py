import pytest
import requests
import json
import config


cities = ['London', 'Moscow', 'Paris', 'New York', 'Tokyo']
urls_common_base = "http://api.openweathermap.org/data/2.5/weather?q="
urls_list = [f'{urls_common_base}{city}&units=metric&appid={config.api_key}' for city in cities]


def is_present(content, key1, key2):
    try:
        content[key1][key2]
    except KeyError:
        return False
    return True


@pytest.mark.parametrize('url', urls_list)
def test_city_has_latitude(url):
    response = requests.get(url)
    response_body = response.json()
    assert is_present(response_body, 'coord', 'lat'), "The key in json doesn't exist. Check the key's names in API"
