from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Data_Ingestion_Config:
    root_dir:Path
    local_data_file:Path
    unzip_data_dir:Path