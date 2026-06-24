from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'pedidos',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Aguardando mensagens no topic 'pedidos'...\n")

for mensagem in consumer:
    pedido = mensagem.value
    print(f"Recebido -> Cliente: {pedido['cliente']} | Produto: {pedido['produto']} | Total: R$ {pedido['total']}")
