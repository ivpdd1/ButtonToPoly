import serial
import socket
import json
import time

ser = serial.Serial('COM13', 9600, timeout=1) // CHANGE THIS TO YOUR PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        line = ser.readline().decode().strip()
        if line == "DOWN":
            sock.sendto(json.dumps({"message": "button pressed"}).encode(), ("YOURTUNNEL.gg", 14011)) // CHANGE THIS TO YOUR TUNNEL URL
            print("button pressed")
        elif line == "UP":
            sock.sendto(json.dumps({"message": "button released"}).encode(), ("YOURTUNNEL.gg", 14011)) // CHANGE THIS TO YOUR TUNNEL URL
            print("button released")
    except:
        pass
    time.sleep(0.01)