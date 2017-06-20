#!/usr/bin/env python
import rospy
import geometry_msgs.msg
import math
from IvyCalibrationNode import *
from ivy.std_api import *


comm=IvyCalibrationNode()
comm.IvyInitStart()

try:
    while True:
        #do nothing
        pass
        #print('test')
except KeyboardInterrupt:
    print('\nROS initialization canceled by user')

comm.IvyInitStop()




def sendCopterPose(data):
    global comm
    comm.IvyInitStart()
    comm.IvySendCopterPose(5, data.x, data.y, data.theta)
    comm.IvyInitStop()
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('IvyCopterPose', anonymous=True)
    

    rospy.Subscriber("copters/0/pose", geometry_msgs.msg.Pose2D, sendCopterPose)
    #time.sleep(0.5)
	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


    
    

#if __name__ == '__main__':

#    listener()

