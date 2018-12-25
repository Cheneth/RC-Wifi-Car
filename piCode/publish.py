import paho.mqtt.publish as publish

publish.single("test/run", "Hello", hostname="test.mosquitto.org")
print("Finished")
