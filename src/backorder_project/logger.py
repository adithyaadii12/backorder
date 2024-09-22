import logging
from datetime import date
from pathlib import Path

LOG_DIR_PATH = Path('logs')
LOG_DIR_PATH.mkdir(exist_ok=True)

LOG_FILE_PATH = LOG_DIR_PATH / (date.today().strftime('%d-%m-%Y') + '.log')

logging.basicConfig(
    
    format="[ %(asctime)s ] %(filename)s:[%(lineno)d] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers= [ 
        logging.FileHandler(LOG_FILE_PATH)
    ]
)


