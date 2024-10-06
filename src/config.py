from pathlib import Path
from typing import Literal

STORED_MODEL_PATH = Path('stored_models')
PREDICTION_TYPE: Literal['regression', 'classification'] = 'classification'
BASE_DATA_NAME = 'filtered_top100k_and_bot100k_backorder_dataset.csv'
TARGET_COLUMN = 'went_on_backorder'