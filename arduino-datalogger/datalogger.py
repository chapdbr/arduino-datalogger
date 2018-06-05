import serial
import struct
import time
import datetime
import msvcrt
from math import sqrt, fabs

ser = serial.Serial()
ser.baudrate = 115200 # baud rate de l'arduino
ser.port = 'COM3' # port de l'arduino
ser.open()
print("Serial is open: ")
print(ser.is_open)
filename = "Log_"+datetime.datetime.now().strftime("%Y-%B-%d_%I-%M-%p")+".txt"
log = open(filename, 'w+')

while True:
	log.write(bytes.decode(ser.readline()))
	ser.flushInput()
	if msvcrt.kbhit():
		if ord(msvcrt.getch()) == 27:
	    		break
log.close()
ser.close()
print("Done.")