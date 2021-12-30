# import the required libraries
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# defining the default arguments dictionary
args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 12, 30),
    'retries': 1,
    "retry_delay": timedelta(seconds=10),
}

dag = DAG('Assignment_1', default_args=args)

task1 = BashOperator(task_id='create_directory', bash_command='mkdir ~/dags/test_dir', dag=dag)

task2 = BashOperator(task_id='get_shasum', bash_command='shasum ~/dags/test_dir', dag=dag)

task2.set_upstream(task1)
