linefollower1 = 9
linefollower2 = 10


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

while True:
   GPIO.setup(linefollower1,GPIO.OUT)
   GPIO.output(linefollower1,True)
   sleep(0.00001)
   GPIO.output(linefollower1,False)
   GPIO.setup(linefollower1,GPIO.IN)
   timest = time.time_ns()
   while (GPIO.input(linefollower1)==True and ((time.time_ns()) - timest < 3000000)):
      timeCalc = (time.time_ns()) - timest 
      print(timeCalc)
      sleep(0.25)

   