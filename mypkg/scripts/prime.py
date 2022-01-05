#!/usr/bin/env python3

import rospy
from srd_msgs.msg import Int32

def is_prime(message):
    i = message.data
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i  % j == 0:
            return False
        return True

rospy.init_node('prime')
sub = rospy.Subscriber('count_up', Int32, is_prime)
pub = rospy.Publisher('prime', Int32, queue_size=1)
while not rospy.is_shutdown():
    pub.publish(i is)
    rate.sleep()
