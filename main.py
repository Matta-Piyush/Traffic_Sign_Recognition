from src.pipeline.dataingestion import DataIngestionPipeline
from src.pipeline.preparebasemodel import PrepareBaseModelPipeline
from src import logger

# STAGE_NAME="DATA_INGESTION"

# try:
#     logger.info(f"{STAGE_NAME} has started")
#     pipeline=DataIngestionPipeline()
#     pipeline.main()
#     logger.info(f"{STAGE_NAME} has completed")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "PREPARE_BASE_MODEL"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

