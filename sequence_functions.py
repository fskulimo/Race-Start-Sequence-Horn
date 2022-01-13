import RPi.GPIO as GPIO
import time

PIN = 17

# 5:00 takes 4 sec; 56 sec to 4:00
def five_min():
    cycles = 1
    count = 0
    horn = 3
    delay = 1

    print("5:00")
    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 4:00 takes 4 sec; 56 sec to 4:00
def five_min():
    cycles = 1
    count = 0
    horn = 3
    delay = 1

    print("4:00")
    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 3:00 takes 6 sec; 54 sec to 2:00
def three_min():
    cycles = 3
    count = 0
    horn = 1
    delay = 1

    print("3:00")
    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 2:00 takes 4 sec; 26 sec to 1:30
def two_min():
    cycles = 2
    count = 0
    horn = 1
    delay = 1

    print("2:00")
    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 1:30 takes 5 sec; 25 sec to 1:00
def one_min_thirty_sec():
    cycles = 3
    count = 0
    horn = .5
    delay = .5

    print("1:30")
    
    print("Signal on")
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(1)
    print("Signal off")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(1)

    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 1:00 takes 2 sec; 28 sec to 0:30
def one_min():
    cycles = 1
    count = 0
    horn = 1
    delay = 1

    print("1:00")
    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 0:30 takes 3 sec; 7 sec to 0:20
def thirty_sec():
    cycles = 3
    count = 0
    horn = .5
    delay = .5

    print("0:30")

    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 0:20 takes 2 sec; 8 sec to 0:10
def twenty_sec():
    cycles = 2
    count = 0
    horn = .5
    delay = .5

    print("0:20")

    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 0:10 takes 1 sec; 4 sec to 0:05
def ten_sec():
    cycles = 1
    count = 0
    horn = .5
    delay = .5

    print("0:10")

    while count < (cycles):
        print("Signal on")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        print("Signal off")
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1

# 0:05 takes 5 sec; GO
def five_sec_count():
    cycles = 5
    count = 0
    countdown = 5
    horn = .5
    delay = .5

    while count < (cycles):
        print(countdown)
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1
        countdown -= 1

# GO takes 4 sec
def five_sec_count():
    cycles = 1
    count = 0
    horn = 3
    delay = 1

    while count < (cycles):
        print("GO")
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(horn)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(delay)
        count += 1