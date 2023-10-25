from src.entity.configuration_entity import Data_Ingestion_Config
from src import logger
import shutil
import os
import zipfile

class DataIngestion:
    def __init__(self,config: Data_Ingestion_Config):
        self.config=config
    def fetch_data(self):
        try:
            logger.info(f"Fetching data from dir notebooks/data into file {self.config.local_data_file}")
            shutil.copyfile('notebooks/data/archive.zip',self.config.local_data_file)
            logger.info(f"Fetched data succesfully into file {self.config.local_data_file}")
        except Exception as e:
            raise e    

    def extract_zip_file(self): 
        try:
            unzip_dir_path=self.config.unzip_data_dir
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
                zip_ref.extractall(unzip_dir_path)
            logger.info(f'unzipped {self.config.local_data_file} file into dir {unzip_dir_path} succesfully')
        except Exception as e:
            raise e
            

