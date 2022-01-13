import RPi.GPIO as GPIO
import time
import sequence_functions

PIN = 17
        
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

# Begin 3 minute sequence
print("3 minute sequence begins in\n")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

sequence_functions.three_min()
time.sleep(54)
sequence_functions.two_min()
time.sleep(26)
sequence_functions.one_min_thirty_sec()
time.sleep(25)
sequence_functions.one_min()
time.sleep(28)
sequence_functions.thirty_sec()
time.sleep(7)
sequence_functions.twenty_sec()
time.sleep(8)
sequence_functions.ten_sec()
time.sleep(4)
sequence_functions.five_sec_count()
sequence_functions.go()