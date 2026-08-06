import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from page.page_ui import SchedulePage
import allure
load_dotenv()
URL = "https://teachers.skyeng.ru/schedule"
COOKIE_VALUE = os.getenv("COOKIE")

def setup_driver_with_cookie():
    driver = webdriver.Chrome()
    driver.get("https://teachers.skyeng.ru")
    """Применяем куки перед рефрешем"""
    driver.add_cookie({
        "name": "session_global",
        "value": COOKIE_VALUE,
        "domain": "skyeng.ru"
    })
    driver.refresh()
    return driver


@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на русском языке")
def test_create_rus_event():
    driver = setup_driver_with_cookie()
    try:
        page = SchedulePage(driver)
        page.create_event(title="Дипломка")
        time.sleep(1)
    finally:
        driver.quit()

@allure.feature("ТЕСТ")
@allure.story("Создание события")
@allure.title("Создание личного события на с названием и описанием на английском")
def test_create_eng_event():
    driver = setup_driver_with_cookie()
    try:
        page = SchedulePage(driver)
        page.create_event(title="Diploma", description="Final work")
        time.sleep(1)
    finally:
        driver.quit()

@allure.feature("ТЕСТ")
@allure.story("Изменение масштаба")
@allure.title("Изменение масштаба интерфейса")
def test_change_name_event():
    driver = setup_driver_with_cookie()
    try:
        driver.maximize_window()
        page = SchedulePage(driver, wait_time=5)
        page.change_scale()
        time.sleep(1)
    finally:
        driver.quit()

@allure.feature("ТЕСТ")
@allure.story("Убрать видимость личных событий")
@allure.title("Убрать галочку чтобы личные события непоказывались в расписании")
def test_unplug_event():
    driver = setup_driver_with_cookie()
    try:
        driver.maximize_window()
        page = SchedulePage(driver, wait_time=5)
        page.toggle_hide_personal_events()
        time.sleep(1)
    finally:
        driver.quit()

@allure.feature("ТЕСТ")
@allure.story("Удаление события")
@allure.title("Выбрать нужное событие и удалить")
def test_delete_event():
    driver = setup_driver_with_cookie()
    try:
        driver.maximize_window()
        page = SchedulePage(driver, wait_time=5)
        page.delete_event()
        time.sleep(1)
    finally:
        driver.quit()

