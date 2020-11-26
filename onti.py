#! /usr/bin/env python

import rospy
import math
from clover import srv
from std_msgs.msg import Float64MultiArray

rospy.init_node('junior_check_points')
pub = rospy.Publisher('/sensors', Float64MultiArray)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

data = {(3.64,6.25): [-8, 0.01, 0.04, 2.80, 0.05, 0.04, 0.01, 0.04]}

r = rospy.Rate(10)
while not rospy.is_shutdown():
    telem = get_telemetry(frame_id='aruco_map')

    if not math.isnan(telem.x) and not math.isnan(telem.y):
        min_i = (-1,-1)
        minn = 999999
        for e in data:
            dist = math.sqrt((telem.x-e[0])**2 + (telem.y-e[1])**2)
            if dist < minn:
                minn = dist
                min_i = e
        
        to_pub = Float64MultiArray()
        to_pub.data = data[min_i]
        pub.publish(to_pub)

    r.sleep()