from initializing import BaseInitializing
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait


class Webpage(BaseInitializing):
    _url = ""

    def __init__(self, web_browser):
        BaseInitializing.__init__(self, web_browser)

    def get_webpage(self):
        self.web_browser.get(url=self._url)

    def close_webpage(self):
        self.web_browser.close()

    def get_url(self):
        return self._url

    def set_url(self, new_url):
        self._url = new_url

    def get_an_element(self, method, value):
        elem = self.web_browser.find_element(by=method, value=value)
        return elem

    def get_an_element_by_id(self, id_value):
        return self.get_an_element(method=By.ID, value=id_value)

    def get_an_element_by_name(self, name_value):
        return self.get_an_element(method=By.NAME, value=name_value)

    def get_an_element_by_class(self, class_value):
        return self.get_an_element(method=By.CLASS_NAME, value=class_value)

    def get_an_element_by_xpath(self, xpath_value):
        return self.get_an_element(method=By.XPATH, value=xpath_value)

    def introduce_a_timeout(self, time):
        self.web_browser.implicitly_wait(time_to_wait=time)



