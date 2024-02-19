from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import Base
import allure
import time


class LocatorsMirapolisAuthorization:
    """Локаторы элементов страницы авторизации"""
    INPUT_LOGIN = '//input[@name="user"]'  # локатор поля ввода логина
    INPUT_PASSWORD = '//input[@name="password"]'  # локатор поля ввода пароля
    BUTTON_ENTER = '//button[@id="button_submit_login_form"]'  # локатор кнопки входа в систему
    SHOW_PASSWORD = '//button[@id="show_password"]'  # локатор элемента, показывающего пароль
    FORGOT_PASSWORD = '//table[@class="links-container"]//a'  # локатор кнопки "Забыли пароль?"
    NEW_PASSWORD_PAGE = '//div[@class="info-title"]'  # локатор "Восстановление пароля"
    NAME_USER_GENERAL_PAGE = '//div[@class="avatar-full-name"]'  # локатор юзернэйм Фомина Елена Сергеевна


class Authorization(Base, LocatorsMirapolisAuthorization):
    """Страница авторизации с переходом на последующие страницы"""
    url = 'https://lmslite47vr.demo.mirapolis.ru/mira'   # адрес страницы авторизации
    login = 'fominaelena'  # Логин
    password = '1P73BP4Z'  # Пароль

    #  Getters
    """Получение явного ожидания по вышеуказанным локаторам"""

    def get_input_login(self):  # Поле ввода логина
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_LOGIN)))

    def get_input_password(self):  # поле ввода пароля
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_PASSWORD)))

    def get_button_enter(self):  # кнопка входа в систему
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER)))

    def get_show_password(self):  # элемент показывающий пароль
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.SHOW_PASSWORD)))

    def get_forgot_password(self):  # кнопка забыли пароль
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.FORGOT_PASSWORD)))

    def get_new_password(self):  # Восстановление пароля
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_PASSWORD_PAGE)))

    def get_user_name(self):  # юзернейм Фомина Елена Сергеевна
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NAME_USER_GENERAL_PAGE)))

    #  Actions
    """Действия"""

    def input_login(self, login):
        """Ввод логина"""
        self.get_input_login().send_keys(login)
        print('Input login')

    def input_password(self, password):
        """Ввод пароля"""
        self.get_input_password().send_keys(password)
        print('Input password')

    def click_button_enter(self):
        """Клик кнопки входа в систему"""
        self.get_button_enter().click()
        print('Button "ВОЙТИ" click')

    def show_password(self):
        """"Показать введенный пароль"""
        self.get_show_password().click()
        print('Нажата кнопка показать пароль')

    def click_button_forgot_password(self):
        """Клик забыли пароль?"""
        self.get_forgot_password().click()
        print('Button "забыли пароль?" click')

    def check_enter_system(self):
        """"Проверка успешного входа в систему"""
        try:
            self.assert_word(self.get_user_name(), 'Фомина Елена Сергеевна')
            self.screenshot()
            print('Вход в систему успешен')
        except AssertionError:
            self.screenshot()
            print('Что-то пошло не так, смотри скриншот')

    #  Methods

    def authorization(self):
        """Штатная авторизация с валидными данными"""
        with allure.step('authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_login(self.login)
            self.input_password(self.password)
            self.click_button_enter()
            time.sleep(3)
            self.check_enter_system()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='authorization')

    def authorization_and_show_password(self):
        """Штатная авторизация с нажатием элемента показывающего пароль"""
        with allure.step('authorization and show password'):
            Logger.add_start_step(method='authorization_and_show_password')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_login(self.login)
            self.input_password(self.password)
            self.show_password()
            self.screenshot()
            time.sleep(3)
            self.click_button_enter()
            time.sleep(3)
            self.check_enter_system()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='authorization_and_show_password')

    def authorization_and_forgot_password(self):
        """Авторизация с нажатием на кнопку "Забыли пароль" и переходом на страницу восстановления пароля"""
        with allure.step('authorization and forgot password'):
            Logger.add_start_step(method='authorization_and_forgot_password')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_login(self.login)
            self.click_button_forgot_password()
            self.assert_word(self.get_new_password(), 'Восстановление пароля')
            self.screenshot()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='authorization_and_forgot_password')

    def authorization_no_valid(self):
        """Негативная проверка. Попытка авторизации невалидными данными"""
        with allure.step('authorization no valid'):
            Logger.add_start_step(method='authorization_no_valid')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_login('qwмолотс')
            self.input_password('0988nbggj,')
            self.click_button_enter()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='authorization_no_valid')
