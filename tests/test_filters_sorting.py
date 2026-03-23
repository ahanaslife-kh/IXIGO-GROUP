from pages.train_home_page import TrainHomePage
from pages.train_result_page import TrainResultPage


def setup_search(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("kol", "Kolkata")
    home.click_search()
    return TrainResultPage(driver)


def test_tatkal_filter(driver):
    result = setup_search(driver)
    result.apply_filters()


def test_best_available_filter(driver):
    result = setup_search(driver)
    result.apply_filters()


def test_ac_only_filter(driver):
    result = setup_search(driver)
    result.apply_filters()


def test_select_result_date(driver):
    result = setup_search(driver)
    result.select_result_date("Sat, 28")


def test_scroll_results(driver):
    result = setup_search(driver)
    result.scroll_to_results()


def test_select_train(driver):
    result = setup_search(driver)
    result.select_train("Poorva")
