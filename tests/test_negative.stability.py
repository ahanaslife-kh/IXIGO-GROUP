from pages.train_home_page import TrainHomePage
from pages.train_pnr_enquiry import TrainPNRPage


def test_empty_search(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.click_search()

    assert home.is_text_present_on_page("Enter Origin")


def test_invalid_pnr(driver):
    pnr = TrainPNRPage(driver)
    pnr.redirect_to_trains()
    pnr.navigate_to_pnr_section()
    pnr.enter_pnr_number("1234567890")
    pnr.click_check_pnr()

    assert pnr.is_invalid_pnr_displayed()


def test_same_source_destination(driver):
    home = TrainHomePage(driver)
    home.open_trains_module()
    home.select_origin("del", "New Delhi")
    home.select_destination("del", "New Delhi")
    home.click_search()

    assert home.is_text_present_on_page("same")
