from src.pipeline.dataingestion import DataIngestionPipeline
from src import logger

STAGE_NAME="DATAINGESTION"

try:
    logger.info(f"{STAGE_NAME} has started")
    pipeline=DataIngestionPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} has completed")
except Exception as e:
    logger.exception(e)
    raise e

