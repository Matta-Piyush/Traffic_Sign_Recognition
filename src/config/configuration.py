from src.constants import *
from src.utils.common import read_yaml,create_directories
from src.entity.configuration_entity import Data_Ingestion_Config,Prepare_Base_Model_Config
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
    
    def get_prepare_base_model_config(self)->Prepare_Base_Model_Config:
        logger.info('get_prepare_base_model_config method called of class Configuration_Manager')
        config=self.config.prepare_base_model
        create_directories([config.root_dir])
        base_model_config=Prepare_Base_Model_Config(Path(config.root_dir),Path(config.base_model_path),Path(config.updated_base_model_path),self.params.IMAGE_SIZE,self.params.CLASSES,self.params.WEIGHTS,self.params.INCLUDE_TOP,self.params.LEARNING_RATE)
        return base_model_config
  