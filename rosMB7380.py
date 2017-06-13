import tf
import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23

def measureData():
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
        distanceString = str(distance) + " cm"

        GPIO.cleanup()

        return distanceString



if __name__ == '__main__':
        try:
                print("\n Note:")
                print("Publishing Range Sensor MB7380 data as STRING 'data'.")

                RangeSensorPub = rospy.Publisher('TX', String, queue_size=1)
                
                RangeSensorPub.publish(measureData())
                rospy.spin()

        
        except KeyboardInterrupt:
                print "Key-interrupt"
                sys.exit(0)

        sys.exit(0)