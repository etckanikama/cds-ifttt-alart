import spidev
import RPi.GPIO as GPIO
import requests
import time

# gpio 17 22 to out
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# SpiDev instance(class)
spi = spidev.SpiDev()

#(port 0 , device 0) spi open
spi.open(0,0)
#max_speed(clock) = 1MHz set
spi.max_speed_hz = 1000000

# 8bit per 1word set
spi.bits_per_word = 8
#dummy data(1111 1111)
dummy = 0xff
#start bits set(0100 0111)
start = 0x47
# single end mode set(0010 0000)
sgl = 0x20
#ch0 select(0000 0000)
ch0 = 0x00
#ch1
ch1 =0x10
#msb mode
msbf = 0x08

#getDateFunction from IC
def getDateFunction(ch):
    # spi interface 
    ad = spi.xfer2([(start + sgl + ch + msbf), dummy])
    # 
    val = ((ad[0]&0x03) << 8) + ad[1]
    # 2bite data to 10bit 
    # voltage = (val* 3.3) / 1023
    return val

# except
try:
    while 1:
        ch1_val = getDateFunction(ch1)
        # print(ch1_val)
        # time.sleep(1)
        if ch1_val > 800:
            #gpio on 17 , 22
            GPIO.output(17, True)
            GPIO.output(22, True)
            # call function
            ch0_val = getDateFunction(ch0)

            value = 1023 - ch0_val
            # submit spreadsheet
            payload= {"value1": value}
            requests.post("https://maker.ifttt.com/trigger/Spreadsheet/with/key/cr6UFQuSffNxwy51dK31a_P77qPLKqPjBoh9dsr-7o3", json=payload)
            if value > 800:
                payload = {"value1": value}
                requests.post("https://maker.ifttt.com/trigger/Spreadsheet/with/key/cr6UFQuSffNxwy51dK31a_P77qPLKqPjBoh9dsr-7o3", json=payload)
        else:
            #gpio off 
            GPIO.output(17, False)
            GPIO.output(22, False)
        time.sleep(10)

except KeyboardInterrupt:
    pass

spi.close()

GPIO.cleanup()
