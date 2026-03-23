import serial
import socket
import json
import time

ser = serial.Serial('COM13', 9600, timeout=1) # CHANGE COM13 TO YOUR PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        line = ser.readline().decode().strip()
        print(line)
        if line == "DOWN":
            sock.sendto(json.dumps({"message": "D"}).encode(), ("impact-rings.gl.at.ply.gg", 14011)) # CHANGE YOUR-TUNNEL.gg TO YOUR TUNNEL URL(WITHOUT A PORT) and 14011 to your port
        elif line == "UP":
            sock.sendto(json.dumps({"message": "U"}).encode(), ("impact-rings.gl.at.ply.gg", 14011)) # CHANGE YOUR-TUNNEL.gg TO YOUR TUNNEL URL(WITHOUT A PORT) and 14011 to your port
    except:
        pass
    time.sleep(0.01)