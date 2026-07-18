import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

#load the local .env file 
load_dotenv(override=True)

class PipelineConfig:
    def __init__(self,config_path: str='/home/abhishek/projects/python_prep/config.yaml'):
        self.env = os.environ.get('ENV_TYPE',{}).lower()
        with open(Path(config_path)) as configfile:
            raw_config = yaml.safe_load(configfile)

        self.global_setting = raw_config.get("global",{})
        self.local_settings = raw_config.get(self.env,{})

        if isinstance(self.local_settings,str):
            self.local_settings = {}

        if not self.local_settings:
            raise ValueError(f"Target env {self.env} is not found in {config_path}")
        
        self.app_name = self.global_setting.get('app_name')
        self.log_dir = self.global_setting.get('log_dir')
        self.db_name = self.local_settings.get('db_name')
        self.host_name = self.local_settings.get('db_host')
        self.port = self.local_settings.get('db_port')
        self.retry_count = self.local_settings.get('max_retry')
        self.log_level = self.local_settings.get('log_level')

        # enforce strict setting for db password
        try:
            self.db_pwd = os.environ['db_pwd']
        except KeyError as e:
            print(f'DB_PWD is not setup it should come from .env file or from system terminal')
            exit(1)

if __name__ == '__main__':
    config = PipelineConfig()
    print(f'Loaded app name: {config.app_name}')
    print(f'Active env: {config.env}')
    print(f"📍 Targeting Host: {config.host_name}")
    print(f"🗄️ Targeting Database: {config.db_name}")
