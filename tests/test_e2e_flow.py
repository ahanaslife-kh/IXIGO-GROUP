# ================== BUS FLOW ==================

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


# ================== TRAIN FLOW ==================

from pages.train_home_page import TrainHomePage
from pages.train_result_page import TrainResultPage
from pages.train_pnr_enquiry import TrainPNRPage
from pages.train_running_status import TrainRunningStatusPage


def test_complete_train_e2e_flow(driver):
    home = TrainHomePage(driver)

    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("kol", "Kolkata")
    home.select_quick_dates()
    home.click_search()

    result = TrainResultPage(driver)

    assert result.select_result_date("Sat, 28"), "Result date not selected"

    result.apply_filters()
    result.scroll_to_results()
    result.select_train("Netaji")
    result.select_coach("3A")
    result.select_quota("General")
    result.select_quota_date_and_book("28")
    result.close_login()

    # ---------- PNR FLOW ----------
    pnr = TrainPNRPage(driver)
    pnr.redirect_to_trains()
    pnr.navigate_to_pnr_section()
    pnr.enter_pnr_number("1234567890")
    pnr.click_check_pnr()

    # ---------- RUNNING STATUS ----------
    running = TrainRunningStatusPage(driver)
    running.redirect_to_trains()
    running.navigate_to_running_status()
    running.enter_train_number("12301")
    running.select_suggestion()
    running.click_check_status()