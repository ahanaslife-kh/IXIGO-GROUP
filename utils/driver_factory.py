from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--start-maximized")

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(
            service=service,
            options=options
        )

        # Fallback maximize (in case option fails)
        driver.maximize_window()

        # Implicit wait
        driver.implicitly_wait(10)

        return driver