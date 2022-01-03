#!/usr/bin/env python3
import rospy
from std_msds.msg import Init32

def cb(message):
    rospy.loginfo(message.data*2)


rospy.init_node('twice')
sub = rospy.subscribe('count_up', Init32, cb)
rospy.spin() #this line mean not end the progrum. if it do not exist, this progrum would end straight away


