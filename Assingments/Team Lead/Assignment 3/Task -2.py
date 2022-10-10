TASK 2:
Write a python code for traffic light system using python(should be communicatable with 
raspberrypi)
Code:
loop = 1
print("TRAFFIC LIGHT SYSTEM")
print("Input Data Catagorization:")
print(" RED:STOP")
print(" YELLOW:GET READY")
print(" GREEN:GO")
print("----------------------------")
loop=eval(input("press 1 to start : "))
while True:
 print("enter input signal colour to run the program : ")
 signal = input()
 if signal == "red":
 print("STOP THE VEHICLE FOR NEXT 60 SECONDS")
 else:
 if signal =="yellow":
 print("get ready")
 else:
 if signal=="green":
 print("go")
 else:
 if signal=="stop":
 print("you choose to end the program")
 else:
 print("enter only the correct signal")

Using RPi library:
import RPi.GPIO as GPIO
import time
import signal
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
def allLightsOff(signal, frame):
 GPIO.output(9, False)
 GPIO.output(10, False)
 GPIO.output(11, False)
 GPIO.cleanup()
 sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)
while True: 
 GPIO.output(9, True) 
 time.sleep(3) 
 GPIO.output(10, True) 
 time.sleep(1) 
 GPIO.output(9, False) 
 GPIO.output(10, False) 
 GPIO.output(11, True) 
 time.sleep(5) 
 GPIO.output(11, False) 
 GPIO.output(10, True) 
 time.sleep(2) 
 GPIO.output(10, False)
