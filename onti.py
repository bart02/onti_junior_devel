#! /usr/bin/env python

import rospy
import math
from clover import srv
from std_msgs.msg import Float32MultiArray

rospy.init_node('junior_check_points')
pub = rospy.Publisher('/sensors', Float32MultiArray)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

data = {(3.64,6.25): [-8, 0.01, 0.04, 2.80, 0.05, 0.04, 0.01, 0.04],
        (1.02,8.07): [-8, 0.05, 0.039, 2.10, 0.03, 0.03, 0.03, 0.03], 
        (3.29,3.06): [-8, 0.06, 0.038, 1.70, 0.05, 0.06, 0.01, 0.04],
        (5.4,0.03): [-8, 0.06, 0.050, 2.00, 0.03, 0.07, 0.03, 0.05]}

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
        
        to_pub = Float32MultiArray()
        to_pub.data = data[min_i]
        pub.publish(to_pub)

    r.sleep()