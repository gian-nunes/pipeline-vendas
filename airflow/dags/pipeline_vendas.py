from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def consumir_e_gravar():
    from kafka import KafkaConsumer
    import json
    
    consumer = KafkaConsumer(
        'vendas_db.public.orders',
        bootstrap_servers='kafka_vendas:29092',
        auto_offset_reset='earliest',
        consumer_timeout_ms=10000,
        group_id='airflow-orders-consumer',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')) if v else None
    )    

    for mensagem in consumer:
        print("=" * 50)
        print(mensagem.value)

    consumer.close()
    print("Terminou de consumir!")    



with DAG(
    dag_id= 'pipeline_vendas',
    start_date=datetime(2026, 1, 1),
    schedule_interval=timedelta(minutes=5),
    catchup=False,
    tags=['vendas', 'cdc'],

)   as dag: 
      tarefa = PythonOperator(
        task_id='consumir_e_gravar',
        python_callable=consumir_e_gravar,
      )
