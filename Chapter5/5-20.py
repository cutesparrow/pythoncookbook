#你想通过串行端口读写数据，典型场景就是和一些硬件设备打交道(比如一个机器人或传感器)。
import serial
ser = serial.Serial('deviceFile')
ser.write()
ser.read()

