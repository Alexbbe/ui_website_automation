from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.firefox.service import Service as Firefox_Service
import sys


class BaseInitializing:
    def __init__(self, web_browser):
        if web_browser == "Chrome":
            self.web_browser = self.__chrome_initializing()
        elif web_browser == "Firefox":
            self.web_browser = self.__firefox_initializing()

    @staticmethod
    def __chrome_initializing():
        if sys.platform == 'win32':
            service = Chrome_Service(executable_path="web_browser_driver/windows/chromedriver.exe")
        elif sys.platform == 'linux1' or sys.platform == 'linux2':
            service = Chrome_Service(executable_path="web_browser_driver/linux/chromedriver")

        web_browser = webdriver.Chrome(service=service)
        return web_browser

    @staticmethod
    def __firefox_initializing():
        if sys.platform == 'win32':
            service = Firefox_Service(executable_path='web_browser_driver/windows/geckodriver.exe')
        elif sys.platform == 'linux1' or sys.platform == 'linux2':
            service = Firefox_Service(executable_path="web_browser_driver/linux/geckodriver")

        web_browser = webdriver.Firefox(service=service)
        return web_browser




