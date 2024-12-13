import logging

def setup_logging(log_file="logs/scraper.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    format = "%(asctime)s - %(levelname)s - %(message)s"
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(format))
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(format))
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)