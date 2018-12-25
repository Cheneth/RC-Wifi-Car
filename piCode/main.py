import paho.mqtt.client as mqtt

move = "Forward"
broker = "m15.cloudmqtt.com"
port = 13613
def on_connect(client, userdata, flags, rc):
    print("Successfully connected with " + str(rc))
    client.subscribe("carbot/server")

def on_message(client, userdata, msg):
    global move
    move = str(msg.payload.decode("utf-8"))
    print(move)

client = mqtt.Client(protocol=mqtt.MQTTv31)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("cdgavfxf", "ORXi9WQE9XJ8")
client.connect("m15.cloudmqtt.com", 13613, 60)

client.loop_start()