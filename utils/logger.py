import logging
import os


def get_logger():
    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("ixigo")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # File handler (append mode)
        file_handler = logging.FileHandler("logs/test.log", mode="a")
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger