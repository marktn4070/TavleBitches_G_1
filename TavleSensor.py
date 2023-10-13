#sensor testdewdee21eqwe
import RPi.GPIO as GPIO
import time
from time import sleep
from sshkeyboard import listen_keyboard

SpeedPin = 32 #Højre
SpeedPin1 = 33 #Venstre
# PWM pins

DirectionPin = 11
DirectionPin1 = 13
DirectionPin2 = 29
DirectionPin3 = 31

linefollower1 = 16
linefollower2 = 18

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering system

GPIO.cleanup()

GPIO.setup(SpeedPin,GPIO.OUT)
GPIO.setup(SpeedPin1,GPIO.OUT)

GPIO.setup(DirectionPin,GPIO.OUT)
GPIO.setup(DirectionPin1,GPIO.OUT)
GPIO.setup(DirectionPin2,GPIO.OUT)
GPIO.setup(DirectionPin3,GPIO.OUT)

pi_pwm = GPIO.PWM(SpeedPin,1000)		#create PWM instance with frequency
pi_pwm.start(0)

pi_pwm1 = GPIO.PWM(SpeedPin1,1000)		#create PWM instance with frequency
pi_pwm1.start(0)			

def koer():
    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)
    
    pi_pwm.ChangeDutyCycle(70) #45 #70
    pi_pwm1.ChangeDutyCycle(80) #50 #80
    #sleep(0.1)

def dven():
    GPIO.output(DirectionPin, False)
    GPIO.output(DirectionPin1, False)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)

    pi_pwm.ChangeDutyCycle(80) #50
    pi_pwm1.ChangeDutyCycle(100) #50
    sleep(0.05)


def dhoej():
    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, False)
    GPIO.output(DirectionPin3, False)

    pi_pwm.ChangeDutyCycle(100) #50
    pi_pwm1.ChangeDutyCycle(80) #50
    sleep(0.05)

def TurnLeft():
    print("Turning Left")
    GPIO.output(DirectionPin, False)
    GPIO.output(DirectionPin1, False)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)

    pi_pwm.ChangeDutyCycle(100)
    pi_pwm1.ChangeDutyCycle(100)

def TurnRight():
    print("Turning Right")
    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, False)
    GPIO.output(DirectionPin3, False)

    pi_pwm.ChangeDutyCycle(100)
    pi_pwm1.ChangeDutyCycle(100)

def GoForward():
    print("Going Forward")
    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)

    pi_pwm.ChangeDutyCycle(100)
    pi_pwm1.ChangeDutyCycle(100)

def GoBackward():
    print("reversing")
    GPIO.output(DirectionPin, False)
    GPIO.output(DirectionPin1, False)	

    GPIO.output(DirectionPin2, False)
    GPIO.output(DirectionPin3, False)

    pi_pwm.ChangeDutyCycle(100)
    pi_pwm1.ChangeDutyCycle(100)

def StopBil():
    print("STOP")
    pi_pwm.ChangeDutyCycle(0)
    pi_pwm1.ChangeDutyCycle(0)


def press(key):
    if key == "w":
        GoForward()
    if key == "s":
        GoBackward()
    if key == "a":
        TurnLeft()
    if key == "d":
        TurnRight()
    if key == "f":
        StopBil()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(linefollower1,GPIO.IN)
GPIO.setup(linefollower2,GPIO.IN)

try:
   aem = input("Indtast A for auto eller M for manuel")
   if aem == "a":   
      while True:
        Venstre = int (GPIO.input(linefollower1))
        print(Venstre)
        Højre = int (GPIO.input(linefollower2))
        print(Højre)
        if (Venstre == 1 and Højre == 1):
            koer()
        elif(Venstre == 1 and Højre == 0):
            dhoej()
        elif(Venstre == 0 and Højre == 0):
            koer()
        elif(Venstre == 0 and Højre == 1):
            dven()
        else:
            koer()
            print("FEJL")
   elif aem == "m":
      while True:
        listen_keyboard(on_press = press)
   else:
      print("Invalid input!")
except KeyboardInterrupt:
  pass
GPIO.cleanup()