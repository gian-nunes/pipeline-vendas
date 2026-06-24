from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

pedidos = [
    {"id": 1, "cliente": "João Silva",  "produto": "Teclado", "total": 300.00},
    {"id": 2, "cliente": "Maria Souza", "produto": "Monitor", "total": 900.00},
    {"id": 3, "cliente": "Carlos Lima", "produto": "Mouse",   "total": 80.00},
]

for pedido in pedidos:
    producer.send('pedidos', value=pedido)
    print(f"Enviado: {pedido}")
    time.sleep(1)

producer.flush()
print("Todos os pedidos enviados!")
