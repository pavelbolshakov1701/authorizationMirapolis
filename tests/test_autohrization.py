from selenium.common import UnexpectedAlertPresentException
from pages.authorization import Authorization
import allure


@allure.description('test authorization')
def test_authorization(driver):
    """Тест штатной авторизации с использованием валидных данных"""
    enter = Authorization(driver)
    enter.authorization()
    driver.quit()


@allure.description('test authorization and show password')
def test_authorization_and_show_password(driver):
    """Тест штатной авторизации с открытым паролем"""
    enter = Authorization(driver)
    enter.authorization_and_show_password()
    driver.quit()


@allure.description('test authorization and forgot password')
def test_authorization_and_forgot_password(driver):
    """Тест авторизации с нажатием кнопки 'Забыли пароль?'"""
    enter = Authorization(driver)
    enter.authorization_and_forgot_password()
    driver.quit()


@allure.description('authorization no valid')
def test_authorization_no_valid(driver):
    """Негативный тест с использованием невалидных данных"""
    enter = Authorization(driver)
    try:
        enter.authorization_no_valid()
    except UnexpectedAlertPresentException:
        enter.screenshot()
        print('Система отработала корректно. Введены невалидные данные, появление сообщения об ошибке, поля ввода'
              ' логина и пароля окрашены в красный цвет. Смотри скриншот')
    driver.quit()
