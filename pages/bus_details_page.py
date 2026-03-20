from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BusDetailsPage(BasePage):

    SEAT_LAYOUT = (By.XPATH, "//div[contains(@class,'seat')]")

    def is_seat_layout_visible(self):
        seats = self.driver.find_elements(*self.SEAT_LAYOUT)
        return len(seats) > 0
