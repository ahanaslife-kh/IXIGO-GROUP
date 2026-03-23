import os
from datetime import datetime

# Centralized folder
SCREENSHOT_FOLDER = "reports/screenshots"
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)


def take_screenshot(driver, name="failure"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = os.path.join(
        SCREENSHOT_FOLDER,
        f"{name}_{timestamp}.png"
    )

    driver.save_screenshot(file_path)

    return file_path