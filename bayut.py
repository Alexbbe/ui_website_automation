from website import Webpage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium import webdriver


class Bayut(Webpage):
    _url = "https://www.bayut.com/"

    def __init__(self, web_browser):
        Webpage.__init__(self, web_browser=web_browser)
        self.get_webpage()

    def get_search_location_element(self):
        search_element = \
            self.get_a_specific_element(method='xpath',
                                        value='//*[@id="body-wrapper"]/header/div[4]/div/div[2]/div/div[1]/div[2]/div/div/ul/input')
        return search_element

    @staticmethod
    def send_value_to_search_location_element(search_element, value):
        if search_element:
            search_element.send_keys(value)
            return value
        return False

    @staticmethod
    def perform_submit_into_search_location(search_element):
        if search_element:
            search_element.send_keys(Keys.ENTER)
            return True
        return False

    def get_find_button_element(self):
        find_button = self.get_a_specific_element(method='xpath',
                                                  value='//*[@id="body-wrapper"]/header/div[4]/div/div[2]/div/div[2]/a')
        return find_button

    @staticmethod
    def click_find_button(find_button):
        if find_button:
            find_button.click()
            return True
        return False

    def get_scroll_down_element_search(self):
        scroll_element = \
            self.get_a_specific_element(method='xpath',
                                        value='//*[@id="body-wrapper"]/header/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/ul')
        return scroll_element

    def get_change_client_purpose_drop_down_button(self):
        drop_down_button = self.get_a_specific_element(method='class',
                                                       value='eedc221b')
        return drop_down_button


    @staticmethod
    def click_client_purpose_drop_down_button(drop_down_button):
        if drop_down_button:
            drop_down_button.click()
            return True
        return False

    def get_change_client_purpose_variants_element(self):
        client_purpose_variants = self.get_a_specific_element(method='xpath',
                                                              value='//*[@id="body-wrapper"]/header/div[4]/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div')
        return client_purpose_variants

    def get_elements_from_client_purpose_drop(self):
        client_purpose_variants_drop = self.get_a_specific_element(method='xpath', value='//*[@id="body-wrapper"]/header/div[4]/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/span',
                                                                   multiple=True)
        return client_purpose_variants_drop

    @staticmethod
    def check_client_purpose_choices_values(client_purpose_variants_drop):
        if client_purpose_variants_drop:
            if (client_purpose_variants_drop[0] == 'Buy') and (client_purpose_variants_drop[1] == 'Rent'):
                return True
            else:
                return False
        return False

    @staticmethod
    def choose_client_purpose(client_purpose_variants_drop, choice):
        if client_purpose_variants_drop:
            for elem in client_purpose_variants_drop:
                if elem.text == choice:
                    elem.click()
                    return True
        return False

    def get_find_location_results(self):
        find_location_results = \
            self.get_a_specific_element(method='class',
                                        value='ef447dde',
                                        multiple=True)
        return find_location_results

    def get_location_for_each_result(self):
        results_locations = self.get_a_specific_element(method='class',
                                                        value='_7afabd84',
                                                        multiple=True)
        return results_locations

    @staticmethod
    def verify_the_results_location(location, searched_location):
        if location:
            for elem in location:
                if searched_location not in elem.text:
                    return False
            return True
        return False

    def get_popular_searches_container(self):
        popular_searches_container = self.get_a_specific_element(method='xpath', value='//*[@id="body-wrapper"]/main/div[5]/div')
        return popular_searches_container

    def get_popular_searches_type(self):
        popular_searches_type = self.get_a_specific_element(method='xpath', value='//*[@id="body-wrapper"]/main/div[5]/div/div[2]/div[2]/div/div/div', multiple=True)
        return popular_searches_type

    @staticmethod
    def choose_popular_search_type(popular_search_types, type):
        if popular_search_types:
            for elem in popular_search_types:
                if elem.text == type:
                    elem.click()
                    return True
        return False

    def get_popular_searches_variants(self):
        popular_searches_variants = self.get_a_specific_element(method='xpath',
                                                                value='//*[@id="body-wrapper"]/main/div[5]/div/div[2]/div[1]/div[2]/*',
                                                                multiple=True)
        return popular_searches_variants

    def get_dubai_apartments_for_rent_list(self):
        dubai_apartments_for_rent_list = self.get_a_specific_element(method='xpath',
                                                                     value='//*[@id="body-wrapper"]/main/div[5]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/ul/li',
                                                                     multiple=True)
        return dubai_apartments_for_rent_list

    def get_dubai_apartments_for_rent_hyper_links(self, dubai_apartments):
        list1 = list()
        if dubai_apartments:
            for elem in dubai_apartments:
                link_to_apartment = self.get_subelements_of_element(method='xpath', elem=elem, value='.//*')
                list1.append(link_to_apartment)
            print([elem.text for elem in list1])
            return list1

    def get_show_more_button_popular_searches(self):
        show_more_popular_searches = self.get_a_specific_element(method='xpath',
                                                                 value="//*[@id='body-wrapper']/main/div[5]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]"
                                                                 )
        return show_more_popular_searches

    @staticmethod
    def click_show_more_popular_searches(show_more_button):
        if show_more_button:
            show_more_button.click()
            return True
        return False

