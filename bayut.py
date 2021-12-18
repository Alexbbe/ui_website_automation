import selenium.webdriver.common.timeouts
from selenium.webdriver.common.keys import Keys

from website import Webpage
from selenium.common.exceptions import NoSuchElementException


class Bayut(Webpage):
    _url = "https://www.bayut.com/"

    def __init__(self, web_browser):
        Webpage.__init__(self, web_browser=web_browser)
        self.get_webpage()

    def get_change_purpose_element(self):
        self.get_an_element_by_class(class_value='')

    def get_search_location_elemnemt(self):
        search_element = self.get_an_element_by_class(class_value='_6a3a3de9')
        if search_element:
            return search_element
        else:
            return False

    @staticmethod
    def send_value_to_search_loaction_element(search_element, value):
        search_element.send_keys(value)
        return value

    @staticmethod
    def perform_submit_into_search_location(search_element):
        if search_element:
            search_element.submit()

    def get_find_button_element(self):
        try:
            find_button = self.get_an_element_by_class(class_value="f6d94e28")
        except NoSuchElementException:
            find_button = None

        if find_button:
            return find_button
        else:
            return False, "The element doesn't exists"

    def click_find_button(self):
        find_button = self.get_find_button_element()
        if find_button:
            find_button.click()

    def get_scroll_down_element_search(self):
        try:
            scroll_element = self.get_an_element_by_class(class_value='_9a03d150')
        except NoSuchElementException:
            scroll_element = None

        if scroll_element:
            return True, scroll_element
        else:
            return False, f"The scroll element didn't appear."


    def verify_each_element_from_scroll(self):
        pass

    def change_client_purporse(self):
        pass

    def complete_search_location(self):
        pass

    def find_location(self):
        pass

    def verify_locations_results(self):
        pass

bayut1 = Bayut(web_browser='Firefox')
search_elem1 = bayut1.get_search_location_elemnemt()
bayut1.send_value_to_search_loaction_element(search_elem1, value="Dubai Marina")
bayut1.perform_submit_into_search_location(search_elem1)
