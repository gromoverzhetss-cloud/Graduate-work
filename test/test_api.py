import requests
import os
import allure
from dotenv import load_dotenv
load_dotenv()

my_token = os.getenv("MY_TOKEN")
eventId = os.getenv("ID")
base_url = "https://api-teachers.skyeng.ru"
assert my_token, "токен ненайден"

@allure.title("Создание личного события")
@allure.story("Создание личного события")
@allure.feature("API")
def test_create_company():
    my_headers = {
        "Content-Type": "application/json",
        "Cookie": f"token_global={my_token}",
        "Authorization": f"Bearer {my_token}"
    }
    body = {
        "backgroundColor": "#FFF7C7",
        "color": "#FAC641",
        "title": "Дипломка",
        "startAt": "2026-08-19T19:00:00+03:00",
        "endAt": "2026-08-19T19:30:00+03:00"
    }

    resp = requests.post(
        f"{base_url}/v2/schedule/createPersonal",
        json=body,
        headers=my_headers
    )

    assert resp.status_code == 200


@allure.story("Переименовать событие")
@allure.feature("API")
@allure.title("Изменение названия личного события")
def test_rename_company():
    my_headers = {
        "Content-Type": "application/json",
        "Cookie": f"token_global={my_token}"
    }
    with allure.step("В теле указываем ID нужного события"):
     body = {
        "id": {eventId},
        "backgroundColor": "#FFF7C7",
        "color": "#FAC641",
        "title": "Дипломка 2",
        "startAt": "2026-08-19T19:00:00+03:00",
        "endAt": "2026-08-19T19:30:00+03:00"
    }

    resp = requests.post(
        f"{base_url}/v2/schedule/updatePersonal",
        json=body,
        headers=my_headers
    )

    assert resp.status_code == 200

@allure.feature("API")
@allure.title("Создание личного события продолжительностью в 23ч59мин")
@allure.story("Создание личного события")
def test_max_time_company():
    my_headers = {
        "Content-Type": "application/json",
        "Cookie": f"token_global={my_token}"
    }
    body = {
        "backgroundColor": "#FFF7C7",
        "color": "#FAC641",
        "title": "Дипломка 3",
        "startAt": "2026-08-19T00:00:00+03:00",
        "endAt": "2026-08-19T23:59:00+03:00"
    }

    resp = requests.post(
        f"{base_url}/v2/schedule/createPersonal",
        json=body,
        headers=my_headers
    )

    assert resp.status_code == 200



@allure.feature("API")
@allure.title("Создание личного события продолжительностью в 25мин01сек")
@allure.story("Создание личного события")
def test_min_time_company():
    my_headers = {
        "Content-Type": "application/json",
        "Cookie": f"token_global={my_token}"
    }
    body = {
        "backgroundColor": "#FFF7C7",
        "color": "#FAC641",
        "title": "Дипломка 4",
        "startAt": "2026-08-19T12:00:00+03:00",
        "endAt": "2026-08-19T12:25:01+03:00"
    }

    resp = requests.post(
        f"{base_url}/v2/schedule/createPersonal",
        json=body,
        headers=my_headers
    )

    assert resp.status_code == 200

@allure.feature("API")
@allure.story("Удаление личного события")
def test_del_company():
     my_headers = {
         "Content-Type": "application/json",
         "Cookie": f"token_global={my_token}",
         "Authorization": f"Bearer {my_token}"
     }
     with allure.step("В теле указываем ID нужного события"):
      body = {
         "id":f"{eventId}",
         "startAt": "2026-08-19T12:00:00+03:00"
     }

     resp = requests.post(
         f"{base_url}/v2/schedule/removePersonal",
         json=body,
         headers=my_headers
     )

     assert resp.status_code == 200