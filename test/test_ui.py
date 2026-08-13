import pytest
from page.page_ui import SchedulePage
import allure


@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на русском языке")
@pytest.mark.test_ui
def test_create_rus_event(auth):
    try:
        page = SchedulePage(auth)
        page.create_event_rus(title="Дипломка")
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на с названием и описанием на английском")
@pytest.mark.test_ui
def test_create_eng_event(auth):
    try:
        page = SchedulePage(auth)
        page.create_event_en(title="Diploma", description="Final work")
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Изменение масштаба")
@allure.title("Изменение масштаба интерфейса")
@pytest.mark.test_ui
def test_change_name_event(auth):
    try:
        page = SchedulePage(auth, wait_time=5)
        page.change_scale()
    finally:
        auth.quit()

@allure.feature("ТЕСТ")
@allure.story("Убрать видимость личных событий")
@allure.title("Убрать галочку чтобы личные события не показывались в расписании")
@pytest.mark.test_ui
def test_unplug_event(auth):
    try:
        page = SchedulePage(auth, wait_time=5)
        page.toggle_hide_personal_events()
    finally:
        auth.quit()



