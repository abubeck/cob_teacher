#!/usr/bin/env python
import roslib;
import rospy
import tf
import math

from tf.msg import tfMessage
from std_msgs.msg import String 
from geometry_msgs.msg import PoseStamped
#############################################

def broadcast_default_handle_frame():

    # init ROS node
    rospy.init_node('broadcast_default_handle_frame')
    
    # start transform boradcaster
    br = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        # describing "/default_handle_link" wrt "/base_link"
        br.sendTransform((0.64, 0.0, 0.0),
                        tf.transformations.quaternion_from_euler(0, 0, -1.57079),
                        rospy.Time.now(),
                        "/default_handle_frame",
                        "/base_link")

        rospy.sleep(0.030)
    
if __name__ == '__main__':
    try:
        broadcast_default_handle_frame()
    except rospy.ROSInterruptException:
        pass