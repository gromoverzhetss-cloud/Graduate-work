import pytest
import requests
import os
import allure
from dotenv import load_dotenv
load_dotenv()


my_token = os.getenv("MY_TOKEN")
my_headers = {
        "Content-Type": "application/json",
        "Cookie": f"token_global={my_token}"
    }
eventId = os.getenv("ID")
base_url = "https://api-teachers.skyeng.ru"
assert my_token, "токен ненайден"

@allure.title("Создание личного события")
@allure.story("Создание личного события")
@allure.feature("API")
@pytest.mark.test_api
def test_create_event():
    with allure.step("Указываем данные в переменные body и my_headers"):
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
    with allure.step("Проверяем что событие создано"):
         assert resp.status_code == 200
         data = resp.json()
         assert "data" in data
         assert "eventId" in data["data"]


@allure.story("Переименовать событие")
@allure.feature("API")
@allure.title("Изменение названия личного события")
@pytest.mark.test_api
def test_rename_event():
    with allure.step("В теле указываем ID нужного события"):
         body = {
            "id": f"{eventId}",
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
    with allure.step("Проверяем что событие изменено"):
         assert resp.status_code == 200
         data = resp.json()
         assert "data" in data
         assert "eventId" in data["data"]

@allure.feature("API")
@allure.title("Создание личного события продолжительностью в 23ч59мин")
@allure.story("Создание личного события")
@pytest.mark.test_api
def test_max_time_event():
    with allure.step("Указываем данные в переменные body и my_headers"):
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
    with allure.step("Проверяем что событие создано"):
         assert resp.status_code == 200
         data = resp.json()
         assert "data" in data
         assert "eventId" in data["data"]

@allure.feature("API")
@allure.title("Создание личного события продолжительностью в 25мин01сек")
@allure.story("Создание личного события")
@pytest.mark.test_api
def test_min_time_event():
    with allure.step("Указываем данные в переменные body и my_headers"):
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
    with allure.step("Проверяем что событие создано"):
         assert resp.status_code == 200
         data = resp.json()
         assert "data" in data
         assert "eventId" in data["data"]

@allure.feature("API")
@allure.story("Удаление личного события")
@pytest.mark.test_api
def test_del_event():
     with allure.step("В теле указываем ID и дату начала нужного события"):
          body = {
             "id": eventId,
             "startAt": "2026-01-19T19:00:00+03:00"
         }
     resp = requests.post(
             f"{base_url}/v2/schedule/removePersonal",
             json=body,
             headers=my_headers
         )
     with allure.step("Проверяем что событие удалено"):
         assert resp.status_code == 200
         assert not eventId