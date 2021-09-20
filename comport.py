import serial
import requests as server
import time
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
portname='Silicon Labs CP210x'
com=''
for port, desc, hwid in sorted(ports):
    if portname in desc:
        com=port
# print(com)

url="http://127.0.0.1/attendance/attendance.php?RFID="
if com!='':
    ser = serial.Serial(com, 115200)
    time.sleep(2)

    while ser.in_waiting:
        val = str(ser.readline().decode().strip('\r\n'))
        print(val)
        if(len(val)>1):
            res=server.get(url+val)
            # print(res.text)
            ser.write(res.text.encode())
            ser.
        time.sleep(2)

