from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HotelSearchNegativePage(BasePage):

    CITY_INPUT = (By.XPATH, "//input[@placeholder='Enter city, area or property name']")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='body-md text-center text-primary']")  # adjust if locator changes

    def search_invalid_city(self, invalid_city_name):
        self.wait.until(EC.element_to_be_clickable(self.CITY_INPUT)).click()

        city_box = self.wait.until(EC.presence_of_element_located(self.CITY_INPUT))
        city_box.clear()
        city_box.send_keys(invalid_city_name)

        error = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        print("Error message displayed:", error.text)
        return error.text