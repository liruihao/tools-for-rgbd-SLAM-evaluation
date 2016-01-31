#! /usr/bin/python
import roslib
import sys
import rospy
import cv2
import numpy as np
import pdb
from matplotlib import pyplot as plt
from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import TransformStamped
from cv_bridge import CvBridge, CvBridgeError
import os

class image_converter():
    def __init__(self):
#        cv2.namedWindow('Image color')
#        cv2.namedWindow('Image depth')
        self.bridge = CvBridge()
        self.image_sub_color = rospy.Subscriber("/camera/rgb/image_raw",Image, self.callback_color)
        self.image_sub_depth = rospy.Subscriber("/camera/depth/image_raw", Image, self.callback_depth)
        self.groundtruth_sub = rospy.Subscriber("/vicon/Xtion/Xtion", TransformStamped, self.callback_groundtruth)
        rospy.rostime.set_rostime_initialized( True )
        print 'SALM recorder is waiting for Image and Vicon.'

    def callback_color(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError, e:
            print e
        time = rospy.rostime.get_time()
#        cv2.imshow('Image color', cv_image)
#        cv2.waitKey(1)
        cv2.imwrite('./Data/rgb/'+str("%10.6f"%time)+'.png', cv_image)
            
    def callback_depth(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'passthrough')
        except CvBridgeError, e:
            print e
        time = rospy.rostime.get_time()
        cv2.imwrite('./Data/depth/'+str("%10.6f"%time)+'.png', cv_image)

    def callback_groundtruth(self, data):
	wx = data.transform.translation.x
	wy = data.transform.translation.y
	wz = data.transform.translation.z
	qx = data.transform.rotation.x
	qy = data.transform.rotation.y
	qz = data.transform.rotation.z
	qw = data.transform.rotation.w
        groundtruthfile = open('./Data/groundtruth.txt', 'a')	
	time = rospy.rostime.get_time()
        print >> groundtruthfile, "%f %f %f %f %f %f %f %f" %(time, wx, wy, wz, qx, qy, qz, qw)
    
if __name__=='__main__':
    ic = image_converter()
    rospy.init_node('SALM_Recorder', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "shutting down"
	groundtruthfile.close()
#    cv2.destroyAllWindows()
