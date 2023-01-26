#!/usr/bin/env python

# OpenCV Tutorial : https://docs.opencv.org/master/d6/d00/tutorial_py_root.html

import random
import rospy
import numpy as np
import cv2 as cv
from sensor_msgs.msg import CompressedImage


def callback(dataf):
    # START CODE HERE, TODO: Complete the code

    data = None

    # TODO: Convert string to uint8 using np.fromstring()
    np_arr = None

    image = cv.imdecode(None, cv.IMREAD_COLOR)  # TODO: Fill the None

    cv.imshow('listener', None)  # TODO: Display the image

    cv.waitKey(1)

    # END CODE HERE


def listner():
    rospy.loginfo("I'm listening ...")
    rospy.init_node('listener', anonymous=True)

    # START CODE HERE

    # TODO: Create a subscriber to topic '/camera/image_raw/compressed'


    # END CODE HERE

    rospy.spin()


if __name__ == '__main__':
    try:
        listner()
    except rospy.ROSInterruptException:
        pass
