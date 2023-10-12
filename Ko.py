#sensor testdewdee21eqwe
import RPi.GPIO as GPIO
import time
from time import sleep


SpeedPin = 32 #Højre
SpeedPin1 = 33 #Venstre
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

def koer():
    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)


    #start PWM of required Duty Cycle 
    #while True:
        # for duty in range(0,101,1):
        #     pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        #     pi_pwm1.ChangeDutyCycle(duty)
        #     sleep(0.1)
                    
        # for duty in range(100,0,-1):
        #     pi_pwm.ChangeDutyCycle(duty)
        #     pi_pwm1.ChangeDutyCycle(duty)
        #     sleep(0.1)


def dven():
		

    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)



def dhoej():

    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)			

    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)




linefollower1 = 16
linefollower2 = 18


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(linefollower1,GPIO.IN)
GPIO.setup(linefollower2,GPIO.IN)

    




try:
   while True:
        Venstre = int (GPIO.input(linefollower1))
        print(Venstre)
        Højre = int (GPIO.input(linefollower2))
        print(Højre)
        time.sleep(0.1)
except KeyboardInterrupt:
  pass
GPIO.cleanup()


if((linefollower1 == 0) and (linefollower2 == 1)):
    dven()
elif((linefollower1 == 1) and (linefollower2 == 0)):
    dhoej()
elif((linefollower1 == 0) and (linefollower2 == 0)):
    koer()
elif((linefollower1 == 1) and (linefollower2 == 1)):
    koer()
else:
    koer()



