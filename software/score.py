import serial

#opens serial connection to arduino
ser = serial.Serial('/dev/cu.usbserial-10', 57600, timeout=1)
count = 0
info = []

while(True):
    line = ser.readline()
    if line:
        string = line.decode()
        
        # gets rid of debug info
        if(len(info) != 0):
            if(info[0].find("Scoring") != -1):
                info = []
            elif(info[0].find("===") != -1):
                info = []
        
        info.append(string)
        print(info)
        # Here is where we display if a touch as occured
        if(string.find("Locked") != -1):
            info = []
        