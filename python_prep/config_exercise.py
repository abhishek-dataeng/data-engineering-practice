import os
import yaml
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(override=True)

@dataclass
class PipelineConfig:
    batch_size: int
    retry_attempt: int
    db_host:str
    db_pwd:str
    log_level:str = "INFO" # default is info
    
class ConfigError(Exception):
    pass

def load_pipeline_config(fpath: str = '/home/abhishek/projects/python_prep/config_ex.yaml') -> PipelineConfig:
    try:
        with open(fpath,'r') as f:
            config_dict = yaml.safe_load(f) or {}
    except FileNotFoundError as e:
        raise ConfigError(f'File: {fpath} is not available error: {e}')
    
    try:
        return PipelineConfig(
            batch_size = int(config_dict.get('batch_size',1000)),
            retry_attempt = int(config_dict.get('retry_count',3)),
            db_host = os.environ.get('db_host'),
            db_pwd = os.environ['db_pwd'],
            log_level = config_dict.get('log_level'),
        )
    except KeyError as e:
        raise ConfigError(f'Missing required config key {e}') from e

if __name__ == "__main__":
    try:
        res = load_pipeline_config()
        print(f"✅ Success! Batch Size: {res.batch_size}, DB Host: {res.db_host}")
    except ConfigError as ce:
        print(f"❌ Configuration Failed: {ce}")