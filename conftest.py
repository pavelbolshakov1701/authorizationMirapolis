from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def driver():
    """Инициализация драйвера GoogleChrome"""
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\User\\Desktop\\phyton\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    return driver
