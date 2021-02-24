#!/usr/bin/env python

import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
from Tkinter import *

def callback(data):
	i==0
	print(data)
	while i==0:
		if(data.data == False):
			break
			
		else:
			pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
			rate = rospy.Rate(15) # 15hz
						   	
			message = PoseStamped()
			length=5
			message.pose.position.x = 0
			message.pose.position.y = 0
			message.header.frame_id='map'

			while not rospy.is_shutdown():

				if(message.pose.position.x == 0 & message.pose.position.y == 0):
					while (message.pose.position.y != length):
						message.pose.position.y += 1
						pub.publish(message)
						rate.sleep()
					while (message.pose.position.x != length):
						message.pose.position.x += 1
						pub.publish(message)
						rate.sleep()

				elif(message.pose.position.x == length & message.pose.position.y == length):
					while (message.pose.position.y != 0):
						message.pose.position.y -= 1
						pub.publish(message)
						rate.sleep()

					while (message.pose.position.x != 0):
						message.pose.position.x -= 1
						pub.publish(message)
						rate.sleep()


def listen():
    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber('listener', Bool, callback)
    rospy.spin()
	

if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass
