import serial
import time
import string
#this file works with "test_multi_sensors.ino" on teensy
#it print data received over bluetooth

ser = serial.Serial("/dev/rfcomm0", 9600) # check rfcomm0 || rfcomm1

while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline() #get data
        cookedserial = rawserial.decode('utf-8').strip('\r\n') #remove \r\n 
        print(cookedserial) #print clean data
