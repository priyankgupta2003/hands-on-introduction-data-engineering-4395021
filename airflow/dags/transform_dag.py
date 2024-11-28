'''tranform DAG'''
from datetime import datetime, date
from airflow.operators.python import PythonOperator
from airflow import DAG
import pandas as pd


with DAG ('tranform_dag', 
          schedule = None,
          start_date = datetime(2023, 1, 1),
          catchup = False
          ) as dag:
    
    def transform_data():
        today = date.today()
        df = pd.read_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv')
        generic_df = df[df['Type'] == 'generic']
        generic_df['Date'] = today.strftime('%Y-%m-%d')
        generic_df.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-transform-data.csv', index = False)

    
    transform_task = PythonOperator(
        task_id = 'transform_task',
        python_callable=transform_data,
        dag =dag
    )

