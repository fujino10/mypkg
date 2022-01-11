#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

i = 0
c = 0
hoge = 0
def cb(message):
    global i
    i = message.data


def is_prime(i):
    global c
    global hoge
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i  % j == 0:
            return False
    c += 1
    hoge = i
    return True

rospy.init_node('prime')
sub = rospy.Subscriber('count_up', Int32, cb)
pub1 = rospy.Publisher('prime_number', Int32, queue_size=1)
pub2 = rospy.Publisher('prime_count', Int32,queue_size=1 ) 
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    prime_str = "Is number {0} Prime? {1}".format(i,is_prime(i))
    rospy.loginfo(prime_str)
    pub1.publish(hoge)
    pub2.publish(c)
    rate.sleep()
