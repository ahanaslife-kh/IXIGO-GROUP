import json
import pytest
from pages.train_home_page import TrainHomePage
from pages.train_result_page import TrainResultPage


data = json.load(open("data/test_data.json"))


@pytest.mark.parametrize("d", data)
def test_search_data_driven(driver, d):
    home = TrainHomePage(driver)
    result = TrainResultPage(driver)

    home.open_trains_module()
    home.select_origin(d["from_city"][:3], d["from_city"])
    home.select_destination(d["to_city"][:3], d["to_city"])
    home.click_search()

    #assert result.select_train(d["train_name"])


@pytest.mark.parametrize("d", data)
def test_coach_data_driven(driver, d):
    home = TrainHomePage(driver)
    result = TrainResultPage(driver)

    home.open_trains_module()
    home.select_origin(d["from_city"][:3], d["from_city"])
    home.select_destination(d["to_city"][:3], d["to_city"])
    home.click_search()

    result.select_train(d["train_name"])
    # assert result.select_coach(d["coach"])


@pytest.mark.parametrize("d", data)
def test_quota_data_driven(driver, d):
    home = TrainHomePage(driver)
    result = TrainResultPage(driver)

    home.open_trains_module()
    home.select_origin(d["from_city"][:3], d["from_city"])
    home.select_destination(d["to_city"][:3], d["to_city"])
    home.click_search()

    result.select_train(d["train_name"])
    # assert result.select_quota(d["category"])
