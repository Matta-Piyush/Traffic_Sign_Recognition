import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')


file_paths=['.github/workflows/.gitkeep',
            'src/__init__.py',
            'src/utils/__init__.py',
            'src/utils/common.py',
            'src/components/__init__.py',
            'src/pipeline/__init__.py',
            'src/config/__init__.py',
            'src/config/configuration.py',
            'src/entity/__init__.py',
            'src/constants/__init__.py',
            'params.yaml',
            'config/config.yaml',
            'setup.py',
            'templates/index.html',
            'requirements.txt',
            'notebooks/trials.ipynb'
]

for file_path in file_paths:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f'creating directory: {file_dir} for the: {file_name}')
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            logging.info(f'creating empty file: {file_name}')
            pass
    else:
        logging.info(f'{file_name} already exists')



