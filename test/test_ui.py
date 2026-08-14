import pytest
from page.page_ui import SchedulePage
import allure


@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на русском языке")
@pytest.mark.test_ui
def test_create_rus_event(auth):
    page = SchedulePage(auth)
    event_rus = page.create_event_rus(title="Дипломка")
    text = event_rus.text.strip()
    assert text.startswith("Дипломка")
    page.delete_event_rus()


@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на с названием и описанием на английском")
@pytest.mark.test_ui
def test_create_eng_event(auth):
    page = SchedulePage(auth)
    event_en = page.create_event_en(title="Diploma", description="Final work")
    text = event_en.text.strip()
    assert text.startswith("Diploma")
    page.delete_event_en()



@allure.feature("ТЕСТ")
@allure.story("Изменение масштаба")
@allure.title("Изменение масштаба интерфейса")
@pytest.mark.test_ui
def test_change_name_event(auth):
    page = SchedulePage(auth, wait_time=5)
    change = page.change_scale()
    assert change.is_displayed()

@allure.feature("ТЕСТ")
@allure.story("Убрать видимость личных событий")
@allure.title("Убрать галочку чтобы личные события не показывались в расписании")
@pytest.mark.test_ui
def test_unplug_event(auth):
    page = SchedulePage(auth, wait_time=5)
    hide = page.toggle_hide_personal_events()
    assert hide




