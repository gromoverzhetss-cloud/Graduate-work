import os
from dotenv import load_dotenv
from page.page_ui import SchedulePage
import allure
load_dotenv()
URL = "https://teachers.skyeng.ru/schedule"
COOKIE_VALUE = os.getenv("COOKIE")


@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на русском языке")
def test_create_rus_event(auth):
    try:
        page = SchedulePage(auth)
        page.create_event(title="Дипломка")
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на с названием и описанием на английском")
def test_create_eng_event(auth):
    try:
        page = SchedulePage(auth)
        page.create_event(title="Diploma", description="Final work")
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Изменение масштаба")
@allure.title("Изменение масштаба интерфейса")
def test_change_name_event(auth):
    try:
        page = SchedulePage(auth, wait_time=5)
        page.change_scale()
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Убрать видимость личных событий")
@allure.title("Убрать галочку чтобы личные события непоказывались в расписании")
def test_unplug_event(auth):
    try:
        page = SchedulePage(auth, wait_time=5)
        page.toggle_hide_personal_events()
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Удаление события")
@allure.title("Выбрать нужное событие и удалить")
def test_delete_event(auth):
    try:
        page = SchedulePage(auth, wait_time=5)
        page.delete_event()
    finally:
        auth.quit()

