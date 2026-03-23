from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import yaml


class DriverFactory:

    @staticmethod
    def get_driver():
        # Load config
        with open("config/config.yaml") as f:
            config = yaml.safe_load(f)

        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(
            service=service,
            options=options
        )

        # Fallback maximize
        driver.maximize_window()

        # Implicit wait from config
        implicit_wait = config.get("wait", {}).get("implicit", 10)
        driver.implicitly_wait(implicit_wait)

        return driver