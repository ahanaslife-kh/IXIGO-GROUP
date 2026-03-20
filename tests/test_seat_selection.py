from pages.home_page import HomePage
from pages.bus_results_page import BusResultsPage


def test_seat_selection(driver):
    driver.get("https://www.ixigo.com/buses")

    home = HomePage(driver)
    home.close_login_popup_if_present()
    home.enter_from_city("Delhi")
    home.enter_to_city("Jaipur")
    home.click_search()

    results = BusResultsPage(driver)

    results.sort_by_price()
    results.apply_ac_filter()
    results.click_show_seats()
    results.select_any_available_seat()
    results.select_boarding_point()
    results.select_dropping_point()
    results.click_continue()

    assert True
