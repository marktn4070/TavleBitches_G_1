import RPi.GPIO as GPIO

linefollower1 = 24
linefollower2 = 26


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(linefollower1,GPIO.IN)
try:
   while True:
    Venstre = int (GPIO.input(linefollower1))
    print(Venstre)
except KeyboardInterrupt:
  pass
GPIO.cleanup()