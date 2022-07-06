import pika

params = pika.URLParameters(
    "amqps://xjjbbkgb:Vyt7GaMax2oyyBkMiuWUln5OY9HCb0vh@moose.rmq.cloudamqp.com/xjjbbkgb")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="main", body="hello")
