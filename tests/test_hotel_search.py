#
# from pages.home_page import HomePage
# from pages.hotel_search_page import HotelSearchPage
#
#
# def test_hotel_filters_and_sort(driver):
#
#     driver.get("https://www.ixigo.com/")
#     home = HomePage(driver)
#     home.open_hotels()
#     home.enter_city("goa")
#     home.select_date(19, "February", 2026)
#     home.select_date(20, "February", 2026)
#     home.select_guests()
#     home.search()
#
#     search = HotelSearchPage(driver)
#     search.wait_for_results()
#
#     initial_count = search.get_hotel_count()
#     assert initial_count > 0, "Search did not return any hotels"
#
#     search.apply_couple_friendly()
#     search.apply_user_rating()
#     search.apply_parking_facility()
#
#     filtered_count = search.get_hotel_count()
#     assert filtered_count > 0, "Filters removed all hotels"
#
#     search.sort_by_price_low()
#
#
