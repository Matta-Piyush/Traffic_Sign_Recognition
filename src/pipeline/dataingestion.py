from src.config.configuration import Configuration_Manager
from src import logger
from src.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        manager=Configuration_Manager()
        config=manager.get_data_ingestion_config()
        data_ingestion_obj=DataIngestion(config=config)
        data_ingestion_obj.fetch_data()
        data_ingestion_obj.extract_zip_file()

