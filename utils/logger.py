import logging
import os
from datetime import datetime

# Centralized log directory
LOG_DIR = "reports/logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name="ixigo"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        # Dynamic log file (per run)
        log_file = os.path.join(
            LOG_DIR,
            f"execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # File handler
        file_handler = logging.FileHandler(log_file, mode="a")
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger