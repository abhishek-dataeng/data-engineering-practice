import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.environ.get('DB_HOST','localhost')
db_pwd = os.environ['DB_PWD']
print(f'DB HOST: {db_host} DB PWD: {db_pwd}')