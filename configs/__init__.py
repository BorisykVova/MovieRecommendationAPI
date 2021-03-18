from pathlib import Path
from functools import lru_cache

import yaml

from . import schemas
from settings import CONFIG_FILE

CONFIG_DIR = Path(__file__).parent
BASE_FILE = CONFIG_DIR / 'base.yaml'


@lru_cache()
def get_config() -> schemas.Config:
    base_config = schemas.Config(**yaml.safe_load(BASE_FILE.read_text()))
    config_file = CONFIG_DIR / Path(CONFIG_FILE).with_suffix('.yaml')
    spec_config = schemas.Config(**yaml.safe_load(config_file.read_text()))
    config_data = {**base_config.dict(exclude_none=True), **spec_config.dict(exclude_none=True)}
    config = schemas.Config(**config_data)
    return config
