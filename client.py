# nohawk-client.py

import time
import serial
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)


packet = bytearray()
packet.append(0xAE)
packet.append(0xA7)
packet.append(0x04)
packet.append(0x00)
packet.append(0x05)
packet.append(0x09)
packet.append(0xBC)
packet.append(0xBE)

# ser.write(packet)

# data = ser.read()
# print(bytes)

while 1:
        ser.write(packet)  #transmit
        print("sent:     ",  packet, '\n')
        rec = ser.readline()
        print("received: ", rec, '\n')  #receive
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(rec)
        time.sleep(1)
