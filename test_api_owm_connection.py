import pytest
import requests
import config


url = f"http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid={config.api_key}"


def test_check_status_code_is_200():
    response = requests.get(url)
    assert response.status_code == 200, \
        f"Connection not succeded"


def test_check_content_type_is_json():
    response = requests.get(url)
    assert "application/json" in response.headers["Content-Type"], \
        "The response body is not in JSON format"


def test_check_city_name_is_london():
    response = requests.get(url)
    response_body = response.json()
    assert response_body["name"] == "London", \
        "Value of variable 'name' in response's body is not 'London'"
