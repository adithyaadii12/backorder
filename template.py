import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

p_name = "backorder_project"

list_of_files = [
    f"src/{p_name}/__init__.py",
    f"src/{p_name}/components/__init__.py",
    f"src/{p_name}/components/data/__init__.py",
    f"src/{p_name}/components/data/ingestion.py",
    f"src/{p_name}/components/data/transformation.py",
    f"src/{p_name}/components/data/validation.py",
    f"src/{p_name}/components/model/__init__.py",
    f"src/{p_name}/components/model/evaluation.py",
    f"src/{p_name}/components/model/pusher.py",
    f"src/{p_name}/components/model/trainer.py",
    f"src/{p_name}/utils/__init__.py",
    f"src/{p_name}/utils/common.py",
    f"src/{p_name}/config/__init__.py",
    f"src/{p_name}/config/configuration.py",
    f"src/{p_name}/pipeline/__init__.py",
    f"src/{p_name}/pipeline/prediction.py",
    f"src/{p_name}/pipeline/training.py",
    f"src/{p_name}/entity/__init__.py",
    f"src/{p_name}/entity/config_entity.py",
    f"src/{p_name}/entity/artifical_entity.py",
    f"src/{p_name}/constants/__init__.py",
    f"src/{p_name}/predictor.py",
    "setup.py",
    "main.py",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Empty file creation
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")