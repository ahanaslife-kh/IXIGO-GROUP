import os
from datetime import datetime


def take_screenshot(driver, name="failure"):
    # Create directory if not exists
    os.makedirs("reports/screenshots", exist_ok=True)

    # Full timestamp (better uniqueness)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"reports/screenshots/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)

    return file_path