import RPi.GPIO as GPIO
import time
import main
import stream_data as stream
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#initialize channels of each wheel.
       
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)


leftOneA = GPIO.PWM(11, 50)
leftOneB = GPIO.PWM(13, 50)
leftTwoA = GPIO.PWM(15, 50)
leftTwoB = GPIO.PWM(16, 50)
rightOneA = GPIO.PWM(29, 50)
rightOneB = GPIO.PWM(31, 50)
rightTwoA = GPIO.PWM(35, 50)
rightTwoB = GPIO.PWM(37, 50)

leftOneA.start(0)
leftOneB.start(0)
leftTwoA.start(0)
leftTwoB.start(0)
rightOneA.start(0)
rightOneB.start(0)
rightTwoA.start(0)
rightTwoB.start(0)

wheels = [leftOneA, leftOneB, leftTwoA, leftTwoB, rightOneA, rightOneB, rightTwoA, rightTwoB]

def changeSpeed(move, wheels): #wheels = [leftForwardA, leftForwardB, leftBackA, leftBackB, rightFowardA, rightForwardB, rightBackA, rightBackB]
    if move != "Back":
        wheels[1].ChangeDutyCycle(0)
        wheels[3].ChangeDutyCycle(0)
        wheels[5].ChangeDutyCycle(0)
        wheels[7].ChangeDutyCycle(0)

    else:
        wheels[0].ChangeDutyCycle(0)
        wheels[2].ChangeDutyCycle(0)
        wheels[4].ChangeDutyCycle(0)
        wheels[6].ChangeDutyCycle(0)
        
    if move == "Left":
        wheels[0].ChangeDutyCycle(15)
        wheels[2].ChangeDutyCycle(15)
        wheels[4].ChangeDutyCycle(100)
        wheels[6].ChangeDutyCycle(100)
        
    elif move == "Right":
        wheels[0].ChangeDutyCycle(100)
        wheels[2].ChangeDutyCycle(100)
        wheels[4].ChangeDutyCycle(15)
        wheels[6].ChangeDutyCycle(15)
     
    elif move == "Forward":
        wheels[0].ChangeDutyCycle(100)
        wheels[2].ChangeDutyCycle(100)
        wheels[4].ChangeDutyCycle(100)
        wheels[6].ChangeDutyCycle(100)

        
    elif move == "Back":
        wheels[1].ChangeDutyCycle(50)
        wheels[3].ChangeDutyCycle(50)
        wheels[5].ChangeDutyCycle(50)
        wheels[7].ChangeDutyCycle(50)

    else: #if move = None, stop the car.
        for wheel in wheels:
            wheel.ChangeDutyCycle(0)

running = 0
'''
try:
    currentMove = main.move
    t = threading.Thread(target=stream.record)
    t.start()
    while True:
        if main.move != currentMove:
            currentMove = main.move
            changeSpeed(currentMove, wheels)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
'''
leftOneA.stop()
leftOneB.stop()
leftTwoA.stop()
leftTwoB.stop()
rightOneA.stop()
rightOneB.stop()
rightTwoA.stop()
rightTwoB.stop()

GPIO.cleanup()

        