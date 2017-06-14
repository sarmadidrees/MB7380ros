import rospy
import tf
from sensor_msgs.msg import Range
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from std_msgs.msg import String

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23

def measureData():
	pulse_start = 0
	pulse_end = 0
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
        distanceString = distance

        GPIO.cleanup()

        return distanceString



if __name__ == '__main__':
        try:
                print("\nNote:")
                print("Publishing Range Sensor MB7380 data as ros defined publisher '/MB7380/data'.")

                RangeSensorPub = rospy.Publisher('/MB7380/data', Range, queue_size=1)
                rospy.init_node('rangeSensor')
                
                
            	
                while not rospy.is_shutdown():
                		rangeMsg = Range()
                      		rangeMsg.header.stamp = rospy.Time.now()
		            	rangeMsg.header.frame_id = "/base_link"
		            	rangeMsg.radiation_type = 0							#0=ultrasonic, 1=IR
		            	rangeMsg.field_of_view = 0.05
		            	rangeMsg.min_range = 0.0
				rangeMsg.max_range = 5.0
                        	rangeMsg.range = measureData()/100
                        #print string1
                        	RangeSensorPub.publish(rangeMsg)
                #rospy.spin()

        
        except KeyboardInterrupt:
                print "Key-interrupt"
                sys.exit(0)
