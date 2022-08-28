import serial
import time
import string
# This file works with AWS and "BT_LED_BUZZ.ino" on Teensy.
# It first connects to AWS, then collects messages from the
# subscribed topic and send command to teensy via bluetooth

ser = serial.Serial("/dev/rfcomm0", 9600) # check rfcomm0 || rfcomm1
#ser.write(str.encode("LED0")) #Set LED ON to check connection at begining
#ser.write(str.encode("BUZZ0"))

import paho.mqtt.client as mqtt #client start here ----------------------------------------
def on_connect(client, userdata, flags, rc): # func for making connection
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )
    client.subscribe("cmd")
def on_message(client, userdata, msg): # Func for Sending msg
    print(msg.topic+": "+str(msg.payload).strip("b"))
    x = str(msg.payload)
    x= x.strip("b'")
    ser.write(str.encode(x)) #send command to teensy LED1 LED0 BUZZ1 BUZZ0
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("54.193.151.177", 1883, 60)
client.loop_forever()