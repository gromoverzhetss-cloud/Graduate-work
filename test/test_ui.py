import os
from os import rename
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

url = "https://teachers.skyeng.ru/schedule"
cookie = os.getenv("COOKIE")


#создать событие на русском языке
def test_create_rus_event():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://teachers.skyeng.ru")
    driver.add_cookie({
            "name": "session_global",
            "value": cookie,
            "domain": "skyeng.ru"
        })
    driver.refresh()

    add_btn = wait.until(EC.element_to_be_clickable((By.NAME, "add")))
    add_btn.click()

    personal_event = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Личное событие')]"))
        )
    personal_event.click()

    title_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']"))
        )
    title_field.send_keys("Дипломка")

    save_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, '-type-primary') and contains(@class, '-color-brand')]"))
        )
    save_btn.click()
    sleep(1)
    driver.quit()
#Создание события с названием и описанием на английском языке
def test_create_eng_event():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://teachers.skyeng.ru")
    driver.add_cookie({
            "name": "session_global",
            "value": cookie,
            "domain": "skyeng.ru"
        })
    driver.refresh()

    add_btn = wait.until(EC.element_to_be_clickable((By.NAME, "add")))
    add_btn.click()

    personal_event = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Личное событие')]"))
        )
    personal_event.click()

    title_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']"))
        )
    title_field.send_keys("Diploma")

    descr = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "textarea[placeholder='Например: ссылка на вебинар']")))
    descr.send_keys("Final work")

    save_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, '-type-primary') and contains(@class, '-color-brand')]"))
        )
    save_btn.click()
    sleep(1)
    driver.quit()


#Уменьшить масштаб итерфейса
def test_change_name_ivent():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    driver.maximize_window()
    driver.add_cookie({
                    "name": "session_global",
                    "value": cookie,
                    "domain": "skyeng.ru"
                    })
    driver.refresh()
    work = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cog-btn")))
    work.click()

    up_name = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//li[@class='scale-option']")))
    up_name.click()
    sleep(1)
    driver.quit()

#Убрать видимость личных событий
def test_unplug_ivent():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    driver.maximize_window()
    driver.add_cookie({
                    "name": "session_global",
                    "value": cookie,
                    "domain": "skyeng.ru"
                    })
    driver.refresh()
    work = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cog-btn")))
    work.click()

    check = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox")))
    check.click()
    sleep(1)
    driver.quit()



#Удаление события
def test_delete_ivent():
     driver = webdriver.Chrome()
     wait = WebDriverWait(driver,3)
     driver.get(url)
     driver.maximize_window()
     driver.add_cookie({
         "name": "session_global",
         "value": cookie,
         "domain": "skyeng.ru"
     })
     driver.refresh()
     sleep(2)
     clear = wait.until(
         EC.visibility_of_element_located(
         (By.XPATH, "(//div[@class='passed-event-cover'])[11]")))
     clear.click()

     button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".root.-type-secondary.-color-brand.-size-m.-active"))
     )
     button.click()
     sleep(2)
     driver.quit()