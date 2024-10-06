""" Training Pipeline to train the model with new data. """
from pathlib import Path

import sys
sys.path.append('C:\\Users\\adith\\Desktop\\backorder\\src')

from backorder_project import utils
from backorder_project.components import (
    DataIngestion,
    DataTransformation,
    DataValidation,
    ModelEvaluation,
    ModelPusher,
    ModelTrainer,
)


@utils.wrap_with_custom_exception
class Training:
    def initiate(self, main_data_fp: Path | None = None):
        """
        `DataIngestion` -> `DataValidation` -> `DataTransformation`

        `ModelTraining` -> `ModelEvaluation` -> `ModelPusher`

        Finally:
        --------
            Store the models and transformers in Pickle format.
        """
        ingestion_artifact = DataIngestion().initiate(main_data_fp)
        DataValidation().initiate()
        transformation_artifact = DataTransformation().initiate()
        model_trainer_artifact = ModelTrainer().initiate()
        ModelEvaluation(
            ingestion_artifact, transformation_artifact, model_trainer_artifact
        ).initiate()

        ModelPusher(transformation_artifact, model_trainer_artifact).initiate()