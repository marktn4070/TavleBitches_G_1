#sensor test
import RPi.GPIO as GPIO
import time
from time import sleep





#PWM test
import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 32
SpeedPin1 = 33
# PWM pins

DirectionPin = 11
DirectionPin1 = 13
DirectionPin2 = 29
DirectionPin3 = 31

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

GPIO.output(DirectionPin, True)
GPIO.output(DirectionPin1, True)			

GPIO.output(DirectionPin2, True)
GPIO.output(DirectionPin3, True)


#start PWM of required Duty Cycle 
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm1.ChangeDutyCycle(duty)
        sleep(0.1)
                
    for duty in range(100,0,-1):
        pi_pwm.ChangeDutyCycle(duty)
        pi_pwm1.ChangeDutyCycle(duty)
        sleep(0.1)



        #______________Sensor_start_____________
A = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
   GPIO.setup(A,GPIO.OUT)
   GPIO.output(A,True)
   sleep(0.00001)
   GPIO.output(A,False)
   GPIO.setup(A,GPIO.IN)
   timest = time.time_ns()
   while (GPIO.input(A)==True and ((time.time_ns()) - timest < 3000000)):
      timeCalc = (time.time_ns()) - timest 
      print(timeCalc)
      sleep(0.25)
   






        #______________Sensor_slut______________