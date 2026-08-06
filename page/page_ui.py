from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class SchedulePage:
    """Переменные для нахождения элементов"""
    BTN_ADD = (By.NAME, "add")
    SPAN_PERSONAL_EVENT = (By.XPATH, "//span[contains(text(),'Личное событие')]")
    INPUT_TITLE = (By.XPATH, "//input[@placeholder='Например: посмотреть вебинар']")
    TEXTAREA_DESCRIPTION = (By.CSS_SELECTOR, "textarea[placeholder='Например: ссылка на вебинар']")
    BTN_SAVE = (By.XPATH, "//button[contains(@class, '-type-primary') and contains(@class, '-color-brand')]")
    CLICK_EV = (By.XPATH, "(//div[@class='passed-event-cover'])[11]")
    BUT_DEL = (By.CSS_SELECTOR, ".root.-type-secondary.-color-brand.-size-m.-active")
    BTN_SETTINGS = (By.CSS_SELECTOR, ".cog-btn")
    LI_SCALE_OPTION = (By.XPATH, "//li[@class='scale-option']")
    CHECKBOX_HIDE_EVENTS = (By.CSS_SELECTOR, ".checkbox")

    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def open(self, url):
        """Открывает страницу и применяет куки"""
        self.driver.get(url)

    def click_add_event(self):
        with allure.step("Нажимаем на кнопку для создания событий"):
           element = self.wait.until(EC.element_to_be_clickable(self.BTN_ADD))
           element.click()

    def select_personal_event(self):
        with allure.step("Выбираем, создать личное событие"):
            element = self.wait.until(EC.element_to_be_clickable(self.SPAN_PERSONAL_EVENT))
            element.click()

    def create_event(self, title, description=None):
        with allure.step("Ждем и кликаем кнопку добавления"):
            self.click_add_event()
            self.select_personal_event()

        with allure.step("Находим поле для ввода названия"):
            title_field = self.wait.until(EC.visibility_of_element_located(self.INPUT_TITLE))
        with allure.step("Вводим название события"):
            title_field.send_keys(title)

        if description:
            with allure.step("Находим поле для описания"):
                descr_field = self.wait.until(EC.visibility_of_element_located(self.TEXTAREA_DESCRIPTION))
            with allure.step("Вводим текст"):
                descr_field.send_keys(description)

        with allure.step("Жмём на кнопку 'Сохранить'"):
            save_btn = self.wait.until(EC.element_to_be_clickable(self.BTN_SAVE))
            save_btn.click()

        with allure.step("Выдерживаем паузу"):
            self.wait.until(lambda d: not EC.invisibility_of_element(save_btn)(d))

    def change_scale(self):
        with allure.step("Находим иконку шестерёнки и кликаем"):
            settings_btn = self.wait.until(EC.visibility_of_element_located(self.BTN_SETTINGS))
            settings_btn.click()
        with allure.step("Выбираем опцию 'Уменьшить масштаб'"):
            scale_option = self.wait.until(EC.element_to_be_clickable(self.LI_SCALE_OPTION))
            scale_option.click()

    def toggle_hide_personal_events(self):
        with allure.step("Находим иконку шестерёнки и кликаем"):
            settings_btn = self.wait.until(EC.visibility_of_element_located(self.BTN_SETTINGS))
            settings_btn.click()
        with allure.step("Убираем галочку"):
            checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX_HIDE_EVENTS))
            checkbox.click()

    def delete_event(self):
        with allure.step("Находим нужное событие и нажимаем на него"):
            clear = self.wait.until(EC.visibility_of_element_located(self.CLICK_EV))
            clear.click()
        with allure.step("Находим и нажимаем на кнопку удалить"):
            button = self.wait.until(EC.element_to_be_clickable(self.BUT_DEL))
            button.click()
