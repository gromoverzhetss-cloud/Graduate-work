import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv


load_dotenv()
COOKIE_VALUE = os.getenv("COOKIE")
@pytest.fixture
def auth():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.get("https://teachers.skyeng.ru")

    """Применяем куки перед рефрешем"""
    driver.add_cookie({
        "name": "session_global",
        "value": COOKIE_VALUE,
        "domain": "skyeng.ru"
    })
    driver.refresh()
    yield driver
    driver.quit()