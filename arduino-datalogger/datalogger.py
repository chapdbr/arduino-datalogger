import warnings
import serial
import serial.tools.list_ports
import datetime
import msvcrt

arduino_ports = [
	p.device
	for p in serial.tools.list_ports.comports()
	if 'Arduino' in p.description
]

if not arduino_ports:
	raise IOError("No Arduino found")
if len(arduino_ports) > 1:
	warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial()
ser.port = arduino_ports[0]
baudrate = input('Please enter baudrate and press ENTER ')
ser.baudrate = baudrate  # Arduino baud rate
ser.open()

if ser.is_open == False:
	print("Couldn't open serial port. Verify baudrate.")
else:
	print('Connected to Arduino')
	filename = "Log_" + datetime.datetime.now().strftime("%Y-%B-%d_%I-%M-%p") + ".txt"
	log = open(filename, 'w+', 1)
	print('Starting data logging, press ESC key to stop...')

	while True:
		log.write(bytes.decode(ser.readline()))
		if msvcrt.kbhit():
			if ord(msvcrt.getch()) == 27:
				break
log.close()
ser.close()
print("Done, exiting program...")
