from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "abhishek",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

def extract():
    print("Extracting sales data for Walmart and other stores like 7 eleven...")
    print('Testing Git rebase ')

def transform():
    print("Transforming data — calculating revenue...")

def load():
    print("Loading data to warehouse...")

with DAG(
    dag_id="first_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    description="My first ETL DAG",
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3