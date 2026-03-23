from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TrainRunningStatusPage(BasePage):



    SUBMENU_OPTIONS = (
        By.CSS_SELECTOR,
        "div[data-testid='submenu-container']>div>div>div"
    )

    TRAIN_NUMBER_INPUT = (
        By.XPATH,
        "//input[@type='search']"
    )

    SUGGESTION_BOX = (
        By.CSS_SELECTOR,
        "div.seoAutocompleterDesktop_suggestionsBox__puLgh"
    )

    CHECK_STATUS_BUTTON = (
        By.XPATH,
        "//button[text()='Check Live Status']"
    )
    TRAINS_REDIRECT = (
        By.CSS_SELECTOR,
        "div.mainContainer>div a[href='/trains']"
    )


    def navigate_to_running_status(self):
        self.logger.info("Navigating to Running Status section")

        for _ in range(3):  # retry loop
            try:
                options = self.get_elements(self.SUBMENU_OPTIONS)

                for option in options:
                    if "Running" in option.text:
                        self.logger.info("Running Status option found → Clicking")
                        option.click()
                        return True

            except Exception as e:
                self.logger.warning(f"Retrying due to: {e}")

        self.logger.error("Running Status option not found after retries")
        return False

    def enter_train_number(self, train_number):
        self.logger.info(f"Entering train number: {train_number}")
        self.click_element(self.TRAIN_NUMBER_INPUT)
        self.enter_text(self.TRAIN_NUMBER_INPUT, train_number)

    def select_suggestion(self):
        self.logger.info("Selecting train suggestion from autocomplete")
        self.click_element(self.SUGGESTION_BOX)

    def click_check_status(self):
        self.logger.info("Clicking Check Live Status button")
        self.click_element(self.CHECK_STATUS_BUTTON)

    def redirect_to_trains(self):
        self.logger.info("Redirecting back to Trains module from Running Status page")
        self.click_element(self.TRAINS_REDIRECT)
