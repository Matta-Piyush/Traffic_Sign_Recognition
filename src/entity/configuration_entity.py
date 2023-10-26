from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Data_Ingestion_Config:
    root_dir:Path
    local_data_file:Path
    unzip_data_dir:Path

@dataclass(frozen=True)
class Prepare_Base_Model_Config:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    image_size: list
    classes: int
    weights: str
    include_top: bool
    learning_rate: float

