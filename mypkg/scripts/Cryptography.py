#!/usr/bin/env python3

import message_filters
import rospy
from std_msgs.msg import Int32

prime_list = []
i = 0
k = 0

def list_prime(meg1):
    global prime_list
    hold1 = mag1.data
    prime_list = list.append(hold1)

def rand_count(msg2):
    global i, k
    hold2 = msg2.data
    random.seed()
    i = random.randint(0, hold2)
    k = random.randint(0, hold2)

def create_crypthgraphy(i, k):
    hold3 = prime_list[i]
    hold4 = prime_list[k]

    c = hold3 * hold4
    return c

rospy.init_node('Cryptography')
pub = rospy.Publisher('Cryptography', Int32, queue_size=1)
sub1 = message_filters.Subscriber('prime_number', Int32, list_prime)
sub2 = message_filters.Subscriber('prime_count', Int32, rand_count)
rate = rospy.Rate(10)

mf = message_filters.ApproximateTimeSynchronizer([sub1, sub2], queue_size=1)

while not rospy.is_shutdown():
    create_crypthgraphy(i, k)
    rospy.loginfo(c)
    rate.sleep()
