from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HotelDetailPage(BasePage):

    HOTEL_TITLE = (By.XPATH, "//h3[@class='h3 mb-5 break-words lg:mb-0 font-bold']")
    HOTEL_PRICE = (By.XPATH, "(//div[@class='h6 text-right text-primary font-medium'])[1]")
    ROOM_TYPES = (By.XPATH,"//h3[@class='h6 text-primary font-medium']")
    ROOM_PRICES = (By.XPATH, "//div[@class='h6 text-right text-primary font-medium']")


    def get_hotel_title(self):
        return self.get_text(self.HOTEL_TITLE)

    def get_hotel_price(self):
        return self.get_text(self.HOTEL_PRICE)

    def get_room_types_with_prices(self):
        room_elements = self.driver.find_elements(*self.ROOM_TYPES)
        price_elements = self.driver.find_elements(*self.ROOM_PRICES)
        price_elements = price_elements[1:]
        rooms = []

        for room, price in zip(room_elements, price_elements):
            rooms.append({
                "room_type": room.text,
                "price": price.text
            })

        return rooms