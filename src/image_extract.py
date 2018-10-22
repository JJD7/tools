#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Massachusetts Institute of Technology

"""Extract images from a rosbag.
"""

import os
import argparse

import cv2

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output directory.")
    parser.add_argument("image_topic", help="Image topic.")

    args = parser.parse_args()

    print "Extract images from %s on topic %s into %s" % (args.bag_file,
                                                          args.image_topic, args.output_dir)

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 0
    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
	cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BAYER_GR2RGB)
	text = "bluriness = : " + str(cv2.Laplacian(cv_img, cv2.CV_64F).var())
	cv2.putText(cv_img, text, (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv2.imwrite(os.path.join(args.output_dir, "frame%06i.png" % count), cv_img)
        print "Wrote image %i" % count

        count += 1

    bag.close()

    return

if __name__ == '__main__':
    main()


'''Examples
rosrun image_extraction image_extract.py pinocchio_2018-10-15-14-59-17.bag /media/jd/My\ Passport/IUCRC/output/left pinocchio/left_camera/image_raw

rosrun image_extraction image_extract.py /media/jd/My\ Passport/IUCRC/Flight\ Data/10_15_18/pinocchio_2018-10-15-12-49-56.bag /media/jd/My\ Passport/IUCRC/Flight\ Data/10_15_18/pinocchio_2018-10-15-12-49-56/left pinocchio/left_camera/image_raw

'''
