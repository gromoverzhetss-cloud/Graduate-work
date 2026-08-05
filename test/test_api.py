import requests
import os
import allure


my_token = os.getenv("MY_TOKEN")
eventId = os.getenv("COOKIE")
base_url = "https://api-teachers.skyeng.ru"
assert my_token, "токен ненайден"

# Создать личное событие
@allure.feature("Создание личного события")
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


# Переименовать событие
# def test_rename_company():
#     my_headers = {
#         "Content-Type": "application/json",
#         "Cookie": f"token_global={my_token}",
#         "Authorization": f"Bearer {my_token}"
#     }
#     body = {
#         "id": {eventId},
#         "backgroundColor": "#FFF7C7",
#         "color": "#FAC641",
#         "title": "Дипломка 2",
#         "startAt": "2026-08-19T19:00:00+03:00",
#         "endAt": "2026-08-19T19:30:00+03:00"
#     }

#     resp = requests.post(
#         f"{base_url}/v2/schedule/updatePersonal",
#         json=body,
#         headers=my_headers
#     )

#     assert resp.status_code == 200

# # Создать событие длительностью 23ч 59 мин
# def test_max_time_company():
#     my_headers = {
#         "Content-Type": "application/json",
#         "Cookie": f"token_global={my_token}",
#         "Authorization": f"Bearer {my_token}"
#     }
#     body = {
#         "id": {eventId},
#         "backgroundColor": "#FFF7C7",
#         "color": "#FAC641",
#         "title": "Дипломка 3",
#         "startAt": "2026-08-19T00:00:00+03:00",
#         "endAt": "2026-08-19T23:59:00+03:00"
#     }

#     resp = requests.post(
#         f"{base_url}/v2/schedule/createPersonal",
#         json=body,
#         headers=my_headers
#     )

#     assert resp.status_code == 200


# # Создать событие длительностью 25мин 01 сек
# def test_min_time_company():
#     my_headers = {
#         "Content-Type": "application/json",
#         "Cookie": f"token_global={my_token}",
#         "Authorization": f"Bearer {my_token}"
#     }
#     body = {
#         "id": {eventId},
#         "backgroundColor": "#FFF7C7",
#         "color": "#FAC641",
#         "title": "Дипломка 4",
#         "startAt": "2026-08-19T12:00:00+03:00",
#         "endAt": "2026-08-19T12:25:01+03:00"
#     }

#     resp = requests.post(
#         f"{base_url}/v2/schedule/createPersonal",
#         json=body,
#         headers=my_headers
#     )

#     assert resp.status_code == 200


# # Удаление события
# def test_del_company():
#     my_headers = {
#         "Content-Type": "application/json",
#         "Cookie": f"token_global={my_token}",
#         "Authorization": f"Bearer {my_token}"
#     }
#     body = {
#         "id": {eventId},
#         "startAt": "2026-08-19T12:00:00+03:00"
#     }

#     resp = requests.post(
#         f"{base_url}/v2/schedule/removePersonal",
#         json=body,
#         headers=my_headers
#     )

#     assert resp.status_code == 200