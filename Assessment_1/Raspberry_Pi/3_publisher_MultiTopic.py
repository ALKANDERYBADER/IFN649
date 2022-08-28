import serial
import time
import string
import paho.mqtt.publish as publish
# This file works with AWS and "test_multi_sensors.ino" on Teensy
# it first Receives data from teensy via bluetooth.
# then it devides the lines into topics and publish them to
# specific topics on AWS

ser = serial.Serial("/dev/rfcomm0", 9600) #CHECK rfcomm0 || rfcomm1

while True:
    i = 0
    while i < 4:
        if ser.in_waiting > 0:
            rawserial = ser.readline()
            cookedserial = rawserial.decode('utf-8').strip('\r\n')
            
            if i == 0:
                H = cookedserial # Humidity
                #print(i) used for checking index
                print(H)
                publish.single("Humidity", H, hostname="54.193.151.177")
            if i == 1:
                T = cookedserial # Temperature
                #print(i) used for checking index
                print(T)
                publish.single("Temperature", T, hostname="54.193.151.177")
            if i == 2:
                HI = cookedserial # Heat index
                #print(i) used for checking index
                print(HI)
                publish.single("HI", HI, hostname="54.193.151.177")
            if i == 3:
                S = cookedserial # Soil sensor
                #print(i) used for checking index
                print(S)
                publish.single("Soil", S, hostname="54.193.151.177")
                i=0
                break
            i = i +1
        

