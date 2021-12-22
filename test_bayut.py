from bayut import Bayut
from time import sleep
from selenium import webdriver


class TestBayut:
    """
    In this class all UI tests for Bayut will be done.
    To run a test from this suit type the following command in terminal:
                            pytest test_bayut.py::TestBayut::test_name -s -v
    Make sure you are in the directory of this file and also "pytest" library is installed
    """

    def test_bayut1(self):
        # Initialize a Bayut webdriver instance for Chrome browser
        bayut1 = Bayut(web_browser='Chrome')

        drop_down_button_client_purpose = bayut1.get_change_client_purpose_drop_down_button()
        assert drop_down_button_client_purpose, f"The drop button for client purpose doesn't exists"
        # Click the drop down button in order to see the client purpose variants
        bayut1.click_client_purpose_drop_down_button(drop_down_button=drop_down_button_client_purpose)

        # Get the client purpose variants elements
        variant_elements = bayut1.get_elements_from_client_purpose_drop()
        assert variant_elements, f"The client purpose variants couldn't be find"
        # Choose a client purpose type - Rent
        bayut1.choose_client_purpose(variant_elements, choice='Rent')
        search = 'Dubai Marina'

        # Get the search input element
        search_elem = bayut1.get_search_location_element()
        assert search_elem, f"The search element input couldn't be found"
        # Type the wanted value in input element
        bayut1.send_value_to_search_location_element(search_elem, value=search)
        sleep(5)
        # Perform enter in input element
        bayut1.perform_submit_into_search_location(search_elem)

        # Get the find button
        find_button = bayut1.get_find_button_element()
        assert find_button, "The find button couldn't be find"
        # Click on find button
        bayut1.click_find_button(find_button)

        # Get the results locations
        results_locations = bayut1.get_location_for_each_result()
        assert bayut1.verify_the_results_location(results_locations, search)

    def test_bayut2(self):
        # Initialize a Bayut webdriver instance for Chrome browser
        bayut2 = Bayut(web_browser='Firefox')

        # Get popular searches types element
        popular_searches_types = bayut2.get_popular_searches_type()
        assert popular_searches_types, "The popular searches type element doesn't exists"

        # Choose popular search type - To Rent
        bayut2.choose_popular_search_type(popular_search_types=popular_searches_types, type='To Rent')

        # Get show more button element
        show_more_button = bayut2.get_show_more_button_popular_searches()
        assert show_more_button

        # Click on show more button in order to see more properties for each location
        bayut2.click_show_more_popular_searches(show_more_button=show_more_button)

        # Get all dubai apartments for rent
        dubai_apartemts_for_rent = bayut2.get_dubai_apartments_for_rent_list()
        # Get the dubai apartments hyper_links number
        limit = len(bayut2.get_dubai_apartments_for_rent_hyper_links(dubai_apartments=dubai_apartemts_for_rent))

        for i in range(0, limit):
            populare_searches_types = bayut2.get_popular_searches_type()
            assert populare_searches_types
            bayut2.choose_popular_search_type(popular_search_types=populare_searches_types, type='To Rent')
            show_more_button = bayut2.get_show_more_button_popular_searches()
            print(show_more_button)
            assert show_more_button
            if i != 0:
                bayut2.click_show_more_popular_searches(show_more_button=show_more_button)
            sleep(10)
            dubai_apartemts_for_rent = bayut2.get_dubai_apartments_for_rent_list()
            assert dubai_apartemts_for_rent
            list_of_dubai_apartments_hyper_links = bayut2.get_dubai_apartments_for_rent_hyper_links(dubai_apartments=dubai_apartemts_for_rent)
            assert list_of_dubai_apartments_hyper_links
            link = list_of_dubai_apartments_hyper_links[i]
            name_of_location = link.text
            link.click()

            sleep(20)
            assert bayut2.verify_the_results_location(location=bayut2.get_location_for_each_result(),
                                                      searched_location=name_of_location)
            bayut2.go_back_to_previous_page()





