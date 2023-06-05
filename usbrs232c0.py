import serial    #PySerial

dev = "/dev/ttyUSB0"    # device name
rate = 9600    # speed 
ser = serial.Serial(dev, rate, timeout=10)

# string = "Hello World\r\n"
# string = string + ""    # terminator 
ser.write(b'\x0101')    # send commands

res = ser.readline()    # recieve commans
res = res.encode()    # encode
print(res)
