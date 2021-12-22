from initializing import BaseInitializing
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Webpage(BaseInitializing):
    _url = ""
    get_methods = {
        "class": By.CLASS_NAME,
        "id": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH
    }

    def __init__(self, web_browser):
        BaseInitializing.__init__(self, web_browser)

    def __del__(self):
        self.close_webpage()

    def get_webpage(self):
        self.web_browser.get(url=self._url)

    def refresh_webpage(self):
        self.web_browser.refresh()

    def close_webpage(self):
        self.web_browser.close()

    def get_url(self):
        return self._url

    def set_url(self, new_url):
        self._url = new_url

    def get_an_element(self, method, value):
        elem = self.web_browser.find_element(by=Webpage.get_methods[method], value=value)
        return elem

    def get_multiple_elemets(self, method, value):
        elem = self.web_browser.find_elements(by=Webpage.get_methods[method], value=value)
        return elem

    def get_a_specific_element(self, method, value, multiple=False):
        try:
            if multiple:
                element = WebDriverWait(self.web_browser, 50).until(
                    EC.visibility_of_all_elements_located((self.get_methods[method], value)))
            else:
                element = WebDriverWait(self.web_browser, 50).until(
                    EC.visibility_of_element_located((self.get_methods[method], value)))
        except TimeoutException:
            element = None

        return element

    @staticmethod
    def get_subelements_of_element(method, value, elem, multiple=False):
        if elem:
            try:
                if multiple:
                    subelem = elem.find_elements(by=Webpage.get_methods[method], value=value)
                else:
                    subelem = elem.find_element(by=Webpage.get_methods[method], value=value)
            except NoSuchElementException:
                subelem = None

            return subelem

    def introduce_a_timeout(self, time):
        self.web_browser.implicitly_wait(time_to_wait=time)

    def go_back_to_previous_page(self):
        self.web_browser.back()
