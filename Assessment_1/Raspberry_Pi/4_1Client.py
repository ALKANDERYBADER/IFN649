import paho.mqtt.client as mqtt
# this file works with AWS only
# it collects messages from the topics
# the client subscribed to and display it

def on_connect(client, userdata, flags, rc): # func for making connection
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc) )
	client.subscribe("Humidity")
	client.subscribe("HI")
def on_message(client, userdata, msg): # Func for Sending msg
	print(msg.topic+" "+str(msg.payload).strip("b"))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("54.193.151.177", 1883, 60)
client.loop_forever()
