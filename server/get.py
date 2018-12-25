import paho.mqtt.client as mosquitto

def on_connect(client, userdata, flags, rc):
    print("Successfully connected to " + str(rc))
    client.subscribe("test/run")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payLoad))

    print("YES")

client = mosquitto.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
