from src.constants import *
from src.utils.common import read_yaml,create_directories
from src.entity.configuration_entity import Data_Ingestion_Config
from src import logger

class Configuration_Manager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->Data_Ingestion_Config:
        logger.info('get_data_ingestion_config method called of class Configuration_Manager')
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=Data_Ingestion_Config(config.root_dir,config.local_data_file,config.unzip_data_dir)
        return data_ingestion_config
  