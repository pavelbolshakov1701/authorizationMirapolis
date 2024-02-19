from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from base.base_class import Base

from base.base_class import Base
from pages.authorization import Autorization



class Application():

    def __init__(self, driver):
        self.driver = driver
        self.base = Base(driver)
        self.autorization = Autorization(driver)




