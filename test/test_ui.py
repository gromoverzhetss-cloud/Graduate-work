
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()

url = "https://teachers.skyeng.ru/schedule"
cookie = os.getenv("COOKIE")

# Создание события
def test_create_ivent():
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

    driver.find_element(By.NAME, "add").click()
    work = driver.find_element(By.XPATH, "//span[contains(text(),'Личное событие')]")
    work.click()
    field = driver.find_element(By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")
    field.send_keys("Дипломка")

    driver.find_element(By.XPATH, "//button[@class='root -type-primary -color-brand -size-m -active']").click()
    ivent = driver.find_element(By.XPATH, "(//div[@class='passed-event-cover'])[13]")
    assert ivent.is_disolayed()


# Изменение названия события с русского на английский язык
# def test_change_name_ivent():
#     driver = webdriver.Chrome()
#     wait = WebDriverWait
#     driver.get(url)
#     driver.maximize_window()
#     driver.add_cookie({
#         "name": "session_global",
#         "value": "jou9l2koniqflr4c2546jntq53",
#         "domain": "skyeng.ru"
#     })
#     driver.refresh()
#     sleep(4)
#     # (//div[@class='passed-event-cover'])[7]
#     driver.find_element(By.XPATH, "(//div[@class='passed-event-cover'])[7]").click()
#     driver.find_element(By.XPATH, "//button[@class='root -type-primary -color-brand -size-m -active']").click()
#     name_ivent = driver.find_element(By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")
#     name_ivent.clear()
#     sleep(4)
#     name_ivent.send_keys("Diploma")
#     sleep(4)
#     driver.find_element(By.XPATH, "//button[@class='root -type-primary -color-brand -size-m -active']").click()
#     sleep(4)
#     driver.quit()
#
#
# # Добавление описания в существующее событие
# def test_description_ivent():
#     driver = webdriver.Chrome()
#     wait = WebDriverWait
#     driver.get(url)
#     driver.maximize_window()
#     driver.add_cookie({
#         "name": "session_global",
#         "value": "jou9l2koniqflr4c2546jntq53",
#         "domain": "skyeng.ru"
#     })
#     driver.refresh()
#     sleep(4)
#     driver.find_element(By.XPATH, "(//div[@class='passed-event-cover'])[6]").click()
#     driver.find_element(By.XPATH, "//button[@class='root -type-primary -color-brand -size-m -active']").click()
#     sleep(4)
#     driver.find_element(By.TAG_NAME, "textarea").send_keys("Ничего не понимаю")
#     sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".root.-type-primary.-color-brand.-size-m.-active").click()
#     sleep(4)
#     driver.quit()
#
#
# # Изменить расписание, оставить в описании один символ
# def test_change_description_ivent():
#     driver = webdriver.Chrome()
#     wait = WebDriverWait
#     driver.get(url)
#     driver.maximize_window()
#     driver.add_cookie({
#         "name": "session_global",
#         "value": "jou9l2koniqflr4c2546jntq53",
#         "domain": "skyeng.ru"
#     })
#     driver.refresh()
#     sleep(4)
#     driver.find_element(By.XPATH, "(//div[@class='passed-event-cover'])[6]").click()
#     driver.find_element(By.XPATH, "//button[@class='root -type-primary -color-brand -size-m -active']").click()
#     sleep(4)
#     descr = driver.find_element(By.TAG_NAME, "textarea")
#     descr.clear()
#     descr.send_keys("a")
#     sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".root.-type-primary.-color-brand.-size-m.-active").click()
#     sleep(4)
#     driver.quit()
#
#
# # Удаление события
# def test_delete_ivent():
#     driver = webdriver.Chrome()
#     wait = WebDriverWait
#     driver.get(url)
#     driver.maximize_window()
#     driver.add_cookie({
#         "name": "session_global",
#         "value": "jou9l2koniqflr4c2546jntq53",
#         "domain": "skyeng.ru"
#     })
#     driver.refresh()
#     sleep(4)
#     driver.find_element(By.XPATH, "(//div[@class='passed-event-cover'])[6]").click()
#     driver.find_element(By.CSS_SELECTOR, ".root.-type-secondary.-color-brand.-size-m.-active").click()
#     sleep(4)
#     driver.quit()