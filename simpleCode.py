import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23

print "Distance Measurement In Progress"

while True:
	GPIO.setmode(GPIO.BCM)
	#GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	#print "Waiting For Sensor To Settle"
	time.sleep(.05)

	#GPIO.output(TRIG, True)
	#time.sleep(0.00001)
	#GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	#distance = (pulse_duration * 34300)/2.0
	distance = (pulse_duration * 100000)

	distance = round(distance, 2)

	print "Distance:",distance,"cm"

	GPIO.cleanup()
