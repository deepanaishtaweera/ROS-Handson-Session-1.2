#!/usr/bin/env python

# OpenCV Tutorial : https://docs.opencv.org/master/d6/d00/tutorial_py_root.html

import rospy
import numpy as np
from sensor_msgs.msg import CompressedImage
import cv2 as cv


def talker():
    # START CODE HERE

    # TODO: Create publisher to topic /camera/image_raw/compressed
    pub = None

    rospy.init_node('talker_node', anonymous=True)

    # TODO: Read the video in videos folder - Hint: use absolute path using forward slashes
    cap = None

    # Check if video file is opened successfully
    if (cap.isOpened() == False):
        rospy.loginfo("Error opening video file")

    # TODO: Get the FPS Value - Hint : use cv.cap.get()
    fps = None

    rate = rospy.Rate(None)  # TODO: Fill the None

    while not rospy.is_shutdown() and cap.isOpened():

        msg = None  # TODO: Create a msg

        ret, frame = None  # TODO: Read the cap

        if not ret:
            break
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv.imencode('.jpg', frame)[1]).tostring()
        pub.publish(msg)
        rate.sleep()

    cap.release()

    # END CODE HERE


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
