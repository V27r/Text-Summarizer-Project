from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger

def run_stage(stage_name: str, pipeline):
    try:
        logger.info(f">>>>>> {stage_name} started <<<<<<")
        pipeline.main()
        logger.info(f">>>>>> {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    stages = [
        ("Data Ingestion stage", DataIngestionTrainingPipeline()),
        ("Data Validation stage", DataValidationTrainingPipeline()),
        ("Data Transformation stage", DataTransformationTrainingPipeline()),
        ("Model Trainer stage", ModelTrainerTrainingPipeline()),
        ("Model Evaluation stage", ModelEvaluationTrainingPipeline())
    ]

    for stage_name, pipeline in stages:
        run_stage(stage_name, pipeline)
