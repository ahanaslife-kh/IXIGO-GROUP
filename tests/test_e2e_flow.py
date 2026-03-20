from pages.home_page import HomePage
from pages.bus_results_page import BusResultsPage

def test_bus_search_e2e(driver):
    driver.get("https://www.ixigo.com/buses")

    home = HomePage(driver)
    home.close_login_popup_if_present()

    home.enter_from_city("Delhi")
    home.enter_to_city("Jaipur")
    home.click_search()

    results = BusResultsPage(driver)
    assert results.results_visible(), "No buses found"
