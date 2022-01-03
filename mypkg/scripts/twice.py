#!/usr/bin/env python3
import rospy
from std_msds.msg import Init 32

def cb:
    rospy.loginfo(message.data*2)


rospy.init_node('twice')
sub = rospy.Subscribe('count_up', Init32, cb)
rospy.spin() #this line mean not end the progrum. if it do not exist, this progrum would end straight away


