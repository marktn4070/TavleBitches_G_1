import RPi.GPIO as GPIO
import time

linefollower1 = 8
linefollower2 = 9


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(linefollower1,GPIO.IN)
GPIO.setup(linefollower2,GPIO.IN)
try:
   while True:
    Venstre = int (GPIO.input(linefollower1))
    print(Venstre)
    Højre = int (GPIO.input(linefollower2))
    print(Højre)
    time.sleep(1)
except KeyboardInterrupt:
  pass
GPIO.cleanup()