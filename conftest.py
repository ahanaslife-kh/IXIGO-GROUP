import os
from datetime import datetime
import pytest
import yaml

from utils.driver_factory import DriverFactory
from utils.screenshot_utils import take_screenshot


# ---------- CONFIG LOADER ----------

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


@pytest.fixture(scope="session")
def config():
    return load_config()


# ---------- DRIVER FIXTURE ----------

@pytest.fixture(scope="function")
def driver(config):
    driver = DriverFactory.get_driver()

    # Load base URL from config
    base_url = config.get("base_url", "https://www.ixigo.com/")
    driver.get(base_url)

    yield driver

    driver.quit()


# ---------- PYTEST HOOK FOR SCREENSHOT ----------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Attach report to test item
    setattr(item, "rep_" + rep.when, rep)

    # Take screenshot on failure
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            try:
                file_path = take_screenshot(driver, item.name)
                print(f"\n📸 Screenshot saved: {file_path}")
            except Exception as e:
                print(f"\n❌ Screenshot capture failed: {e}")