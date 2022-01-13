import RPi.GPIO as GPIO
import time
import sequence_functions

PIN = 17
        
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

# Begin 5 minute sequence
print("2 minute sequence begins in\n")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

sequence_functions.five_min()
time.sleep(56)
sequence_functions.four_min()
time.sleep(176)
sequence_functions.one_min()
time.sleep(58)
sequence_functions.go()
