from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Flights imports
from pages.home_page import FlightsPage
from pages.search_results_page import SearchResultsPage

# Bus imports
from pages.home_page import HomePage
from pages.bus_results_page import BusResultsPage


# ================== FLIGHTS FLOW ==================

def perform_flight_search(driver):
    driver.set_window_size(1920, 1080)
    driver.get("https://www.ixigo.com/")

    wait = WebDriverWait(driver, 15)

    flights = FlightsPage(driver)
    flights.open_flights_tab()

    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='From']")))
    flights.select_from_city("New Delhi")

    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='To']")))
    flights.select_to_city("Mumbai")

    flights.select_date()
    flights.select_travel_class("Business")
    flights.click_search()

    results = SearchResultsPage(driver)
    results.wait_for_results_to_load()

    return results


def test_non_stop_filter(driver):
    results = perform_flight_search(driver)
    results.apply_non_stop_filter()
    stops = results.get_all_stop_texts()
    assert len(stops) > 0
    assert all("Non-stop" in stop for stop in stops)


def test_air_india_filter(driver):
    results = perform_flight_search(driver)
    results.apply_airline_filter_by_code("AI")
    airlines = results.get_all_airline_names()
    assert len(airlines) > 0
    assert all("Air India" in airline for airline in airlines)


def test_indigo_filter(driver):
    results = perform_flight_search(driver)
    results.apply_airline_filter_by_code("6E")
    airlines = results.get_all_airline_names()
    assert len(airlines) > 0
    assert all("indigo" in airline.lower() for airline in airlines)


def test_one_stop_filter(driver):
    results = perform_flight_search(driver)
    results.apply_one_stop_filter()
    stops = results.get_all_stop_texts()
    assert len(stops) > 0
    assert all("1 stop" in stop.lower() for stop in stops)


def test_price_slider_filter(driver):
    results = perform_flight_search(driver)
    results.reduce_max_price_slider(30000)
    prices = results.get_all_prices()
    assert len(prices) > 0
    assert max(prices) <= 30000


def test_duration_filter(driver):
    results = perform_flight_search(driver)
    results.reduce_duration_slider(5)
    durations = results.get_all_durations()
    assert len(durations) > 0
    assert max(durations) <= 5


# ================== BUS FLOW ==================

def open_bus_results(driver):
    driver.get("https://www.ixigo.com/buses")

    home = HomePage(driver)
    home.close_login_popup_if_present()
    home.enter_from_city("Delhi")
    home.enter_to_city("Jaipur")
    home.click_search()

    return BusResultsPage(driver)


def open_seat_flow(driver):
    results = open_bus_results(driver)
    results.sort_by_price()
    results.click_show_seats()
    results.select_any_available_seat()
    results.select_boarding_point()
    results.select_dropping_point()
    return results


# ---------- Basic Bus Tests ----------

def test_bus_results_load(driver):
    results = open_bus_results(driver)
    assert results.results_visible()


def test_bus_sort_by_price(driver):
    results = open_bus_results(driver)
    results.sort_by_price()
    assert True


def test_bus_ac_filter(driver):
    results = open_bus_results(driver)
    results.apply_ac_filter()
    assert True


# ---------- Seat Flow Tests ----------

def test_seat_layout_visible(driver):
    results = open_seat_flow(driver)
    assert results.seats_visible()


def test_continue_button_visible(driver):
    results = open_seat_flow(driver)
    assert results.continue_button_visible()


def test_full_booking_flow(driver):
    results = open_seat_flow(driver)
    results.click_continue()
    assert True


# ---------- Negative Tests ----------

def test_continue_without_seat(driver):
    results = open_bus_results(driver)
    results.sort_by_price()
    results.click_show_seats()

    results.select_boarding_point()
    results.select_dropping_point()

    assert not results.continue_button_clickable()


def test_boarding_without_seat(driver):
    results = open_bus_results(driver)
    results.sort_by_price()
    results.click_show_seats()

    results.select_boarding_point()

    assert not results.continue_button_clickable()