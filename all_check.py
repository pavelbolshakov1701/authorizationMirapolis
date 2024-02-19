import time

import selenium
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service
from Application.application import Application
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from base.base_class import Base


options = webdriver.ChromeOptions()
# options.page_load_strategy = 'eager'
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\User\\Desktop\\phyton\\resource\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)

driver.get('https://lmslite47vr.demo.mirapolis.ru/mira')
driver.maximize_window()

try:
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user"]'))).send_keys('fominaelen')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys('1P73BP4Z')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="button_submit_login_form"]'))).click()
    time.sleep(5)
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//table[@class="links-container"]//a'))).click()
    value = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="avatar-full-name"]'))).text
    assert value == 'Фомина Елена Сергеевна'
    time.sleep(3)
    driver.quit()
except UnexpectedAlertPresentException:
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user"]'))).send_keys('fominaelena')
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys('1P73BP4Z')
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="button_submit_login_form"]'))).click()
    # time.sleep(5)
    # # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//table[@class="links-container"]//a'))).click()
    # value = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="avatar-full-name"]'))).text
    # assert value == 'Фомина Елена Сергеевна'
    # time.sleep(3)
    # driver.quit()
    b = Base(driver)
    b.screenshot()
    print('Система отработала корректно.Введены невалидные данные, появление сообщения об ошибке')


