import time
import string
import paho.mqtt.publish as publish #publisher start here --------------------------------
# This file works with AWS only
# It publishes commands to cmd topic

i =1 #used for counting loop number
print("loop started")
while (i < 4):
    print("Loop number: "+str(i)+"/3" )
    publish.single("cmd", "LED1", hostname="54.193.151.177") #publishing data to AWS topic
    print("Publishing LED on")
    time.sleep(1)
    publish.single("cmd", "BUZZ1", hostname="54.193.151.177") #publishing data to AWS topic
    print("Publishing BUZZ on")
    time.sleep(1)
    publish.single("cmd", "BUZZ0", hostname="54.193.151.177") #publishing data to AWS topic
    print("Publishing BUZZ off")
    time.sleep(1)
    publish.single("cmd", "LED0", hostname="54.193.151.177") #publishing data to AWS topic
    print("Publishing LED off")
    time.sleep(1)
    i= i+1 #used for counting loop number
print("Loop ended")