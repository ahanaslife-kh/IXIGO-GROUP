from pages.home_page import HomePage
from pages.hotel_detail_page import HotelDetailPage
from pages.hotel_search_page import HotelSearchPage
from pages.HotelSearchNegativePage import HotelSearchNegativePage

def test_e2e_hotel_booking(driver):
    home = HomePage(driver)
    home.open_hotels()
    home.enter_city("goa")
    home.select_date(25, "February", 2026)
    home.select_date(27, "February", 2026)
    home.select_guests()
    home.search()


def test_hotel_filters_and_sort(driver):
    home = HomePage(driver)
    home.open_hotels()
    home.enter_city("Goa")
    home.select_date(25, "February", 2026)
    home.select_date(27, "February", 2026)
    home.select_guests()
    home.search()
    home.close_popup_if_present()
    search = HotelSearchPage(driver)
    search.wait_for_results()

    initial_count = search.get_hotel_count()
    assert initial_count > 0, "Search did not return any hotels"

    search.apply_couple_friendly()
    search.apply_user_rating()
    search.apply_parking_facility()

    filtered_count = search.get_hotel_count()
    assert filtered_count > 0, "Filters removed all hotels"

    search.sort_by_price_low()

    hotel_detail,_ = search.open_first_hotel()
    hotel_detail.switch_to_new_tab()

    title = hotel_detail.get_hotel_title()
    assert title != "", "Hotel detail page did not load properly"



def test_invalid_city_search(driver):
    home = HomePage(driver)
    home.open_hotels()
    negative_search = HotelSearchNegativePage(driver)
    error_text = negative_search.search_invalid_city("asdfghjkl")
    assert error_text != ""



def test_sort_price_high_to_low_validation(driver):
    home = HomePage(driver)
    home.open_hotels()
    home.enter_city("Goa")
    home.select_date(25, "February", 2026)
    home.select_date(27, "February", 2026)
    home.select_guests()
    home.search()

    home.close_popup_if_present()

    search = HotelSearchPage(driver)
    search.wait_for_results()

    search.sort_by_price_high()

    prices = search.get_all_prices()

    assert prices == sorted(prices, reverse=True), "Prices are not sorted high to low"
    print("Prices got sorted high to low")


def test_clear_filters(driver):
    home = HomePage(driver)
    home.open_hotels()
    home.enter_city("Goa")
    home.select_date(25, "February", 2026)
    home.select_date(27, "February", 2026)
    home.select_guests()
    home.search()
    home.close_popup_if_present()
    search = HotelSearchPage(driver)
    search.wait_for_results()
    search.apply_couple_friendly()
    search.apply_user_rating()
    search.apply_star_rating()
    search.apply_parking_facility()
    search.clear_all_filters()

def test_print_hotel_details(driver):
    home = HomePage(driver)
    home.open_hotels()
    home.enter_city("Mauritius")
    home.select_date(25, "February", 2026)
    home.select_date(27, "February", 2026)
    home.select_guests()
    home.search()

    home.close_popup_if_present()

    search = HotelSearchPage(driver)
    search.wait_for_results()
    search.open_first_hotel()

    hotel_detail = HotelDetailPage(driver)
    hotel_detail.switch_to_new_tab()

    name = hotel_detail.get_hotel_title()
    price = hotel_detail.get_hotel_price()
    rooms = hotel_detail.get_room_types_with_prices()

    print("\n******** HOTEL DETAILS *************")
    print("Hotel Name:", name)
    print("Hotel Starting Price:", price)

    print("\n   Types of Rooms Available & Prices:  ")
    for room in rooms:
        print(f"- {room['room_type']} : {room['price']}")













# import json
# import time
#
# from pages.home_page import HomePage
# from pages.hotel_search_page import HotelSearchPage
# from pages.hotel_detail_page import HotelDetailPage
#
# def test_e2e_hotel_booking(driver):
#     # with open("data/test_data.json") as f:
#     #     data = json.load(f)
#
#     # driver.get("https://www.ixigo.com/")
#
#     home = HomePage(driver)
#     home.open_hotels()
#     time.sleep(3)
#     home.enter_city("goa")
#     time.sleep(3)
#     home.select_date(18, "February", 2026)
#     home.select_date(19, "February", 2026)
#     time.sleep(3)
#     home.select_guests()
#     time.sleep(3)
#     home.search()
#     time.sleep(3)
#
#
#     search = HotelSearchPage(driver)
#     search.apply_filters()
#     search.select_first_hotel()
#
#     detail = HotelDetailPage(driver)
#     detail.switch_to_new_tab()
#
#     title = detail.get_hotel_title()
#
#     assert title != "", "Hotel detail page did not load properly"
#
#     # search = HotelSearchPage(driver)
#     # search.apply_filters()
#     # search.select_first_hotel()
#     #
#     # detail = HotelDetailPage(driver)
#     # detail.switch_to_new_tab()