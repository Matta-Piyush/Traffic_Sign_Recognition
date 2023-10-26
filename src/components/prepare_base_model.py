from src.entity.configuration_entity import Prepare_Base_Model_Config
from src import logger
from src.config.configuration import Prepare_Base_Model_Config
import tensorflow
from tensorflow import keras
from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from pathlib import Path
from keras.layers import Dense,Flatten,BatchNormalization,Dropout


class PrepareBaseModel:
    def __init__(self,config:Prepare_Base_Model_Config) -> None:
        self.config=config

    
    @staticmethod
    def save_model(path:Path,model:keras.Model):
        model.save(path)


    def get_base_model(self):
        self.model=VGG16(include_top=self.config.include_top,weights=self.config.weights,input_shape=self.config.image_size)
        logger.info('base model has been downloaded')
        self.save_model(self.config.base_model_path,self.model)
        logger.info(f'base model has been saved at the path {self.config.base_model_path}')
        # print(self.model.summary())
    
   


    @staticmethod
    def prepare_full_model(model:keras.Model,classes:int,freezeall:bool,freezetill:int,learning_rate:float):
        if freezeall:
            model.trainable=False
        elif freezetill is not None and freezetill>0:
            for layers in model.layers[:freezetill]:
                layers.trainable=False

        # print(model.summary())
        updated_model=Sequential()
        updated_model.add(model)
        updated_model.add(Flatten())
        updated_model.add(Dense(128,activation='relu'))
        updated_model.add(BatchNormalization())
        updated_model.add(Dropout(0.1))
        updated_model.add(Dense(64,activation='relu'))
        updated_model.add(BatchNormalization())
        updated_model.add(Dropout(0.1))
        updated_model.add(Dense(classes,activation='softmax'))

        updated_model.compile(optimizer=keras.optimizers.Adam(learning_rate),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
       
        # print(updated_model.summary())
        
        return updated_model



    def update_full_model(self):
        model=self.prepare_full_model(self.model,self.config.classes,False,15,self.config.learning_rate)
        self.save_model(self.config.updated_base_model_path,model)
        logger.info(f'updated base model has been saved at the path {self.config.updated_base_model_path}')

    




