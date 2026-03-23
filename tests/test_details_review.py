from pages.train_home_page import TrainHomePage
from pages.train_result_page import TrainResultPage


def setup_details(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("kol", "Kolkata")
    home.click_search()
    return TrainResultPage(driver)


def test_train_visible(driver):
    result = setup_details(driver)

    assert result.select_train("Poorva")


def test_coach_selection(driver):
    result = setup_details(driver)
    result.select_train("Poorva")
    assert result.select_coach("3A")


def test_quota_selection(driver):
    result = setup_details(driver)
    result.select_train("Poorva")
    assert result.select_quota("General")


def test_quota_date_visible(driver):
    result = setup_details(driver)
    result.select_train("Poorva")
    assert result.select_quota_date("28")
