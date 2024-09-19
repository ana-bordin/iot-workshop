import paho.mqtt.client as mqtt
import time
from sensor import read_sensor_data

broker = "broker.hivemq.com"
port = 1883
topic = "iot/sensor/temperature"

def on_connect(client, userdata, flags, rc):
    print("Conectado com o código de resultado " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)
client.loop_start()

while True:
    temperature = read_sensor_data()
    payload = f"Temperatura: {temperature:.2f} °C"
    client.publish(topic, payload)
    time.sleep(5)