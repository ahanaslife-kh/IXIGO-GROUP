from pages.train_home_page import TrainHomePage
from pages.train_result_page import TrainResultPage


def test_search_with_valid_locations(driver):
    home = TrainHomePage(driver)
    result = TrainResultPage(driver)

    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("kol", "Kolkata")
    home.click_search()

    assert result.is_element_present(result.RESULTS_SECTION)


def test_swap_locations(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("kol", "Kolkata")
    home.swap_locations()
    home.click_search()


def test_select_quick_dates(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("kol", "Kolkata")
    home.select_quick_dates()
    home.click_search()


def test_open_calendar(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.open_calendar()


def test_search_button_clickable(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.click_search()
