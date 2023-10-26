from src.components.prepare_base_model import PrepareBaseModel
from src.config.configuration import Configuration_Manager

class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        manager=Configuration_Manager()
        config=manager.get_prepare_base_model_config()
        obj=PrepareBaseModel(config)
        obj.get_base_model()
        obj.update_full_model()
        
