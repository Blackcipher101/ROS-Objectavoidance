#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    regions = [
    min(min(msg.ranges[0:143]),10),
    min(min(msg.ranges[143:287]),10),
    min(min(msg.ranges[287:431]),10),
    min(min(msg.ranges[431:575]),10),
    min(min(msg.ranges[575:719]),10),
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('reading_laser')

    sub = rospy.Subscriber('/m2wr/laser/scan', LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()
