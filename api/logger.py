import logging

def get_logger(nome):
    logger = logging.getLogger(nome)
    logger.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler("logs/app.log", mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger