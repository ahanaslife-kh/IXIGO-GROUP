from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TrainPNRPage(BasePage):


    SUBMENU_OPTIONS = (
        By.CSS_SELECTOR,
        "div[data-testid='submenu-container']>div>div>div"
    )

    PNR_INPUT = (By.CSS_SELECTOR, "input[type='tel']")

    PNR_SEARCH_BUTTON = (
        By.XPATH,
        "//button[text()='Check PNR Status']"
    )

    INVALID_PNR_MESSAGE = (
        By.XPATH,
        "//p[text()='PNR No. is not valid']"
    )

    TRAINS_REDIRECT = (
        By.CSS_SELECTOR,
        "div.mainContainer>div a[href='/trains']"
    )


    def navigate_to_pnr_section(self):
        self.logger.info("Navigating to PNR section")
        options = self.get_elements(self.SUBMENU_OPTIONS)
        for option in options:
            if "PNR" in option.text:
                self.logger.info("PNR option found → Clicking")
                option.click()
                return True
        self.logger.warning("PNR option not found")
        return False

    def enter_pnr_number(self, pnr_number):
        self.logger.info(f"Entering PNR number: {pnr_number}")
        self.enter_text(self.PNR_INPUT, pnr_number)

    def click_check_pnr(self):
        self.logger.info("Clicking Check PNR Status button")
        self.click_element(self.PNR_SEARCH_BUTTON)

    def is_invalid_pnr_displayed(self):
        self.logger.info("Checking if invalid PNR message is displayed")
        return self.is_text_present_on_page("PNR No. is not valid")

    def redirect_to_trains(self):
        self.logger.info("Redirecting back to Trains module")
        self.click_element(self.TRAINS_REDIRECT)
