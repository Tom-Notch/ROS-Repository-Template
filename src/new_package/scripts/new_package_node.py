#!/usr/bin/env python3
#
# Created on Wed Sep 04 2024 21:06:48
# Author: Mukai (Tom Notch) Yu
# Email: mukaiy@andrew.cmu.edu
# Affiliation: Carnegie Mellon University, Robotics Institute
#
# Copyright Ⓒ 2024 Mukai (Tom Notch) Yu
#
from curses import panel
from enum import IntEnum

import rospy
import tf2_geometry_msgs
import tf2_ros
from file_utils.files import print_dict
from file_utils.files import read_file
from geometry_msgs.msg import PointStamped
from new_package.msg import new_msg
from new_package.new_package_library import NewActionClient

if __name__ == "__main__":
    rospy.init_node("new_package_node", anonymous=True)  # Initialize the node

    try:
        config_path = rospy.get_param("~config_path")
        rospy.loginfo("Config file path: %s" % config_path)
        # Here you can add your logic to open and read the config file
    except KeyError:
        rospy.logerr("Parameter 'config_path' not set")

    config = read_file(config_path)  # Get the file path from the first argument

    rospy.loginfo("Config file content:")
    print_dict(config)  # Print the file content

    # Main control loop
    while not rospy.is_shutdown():
        rospy.loginfo("Node is running")
        rospy.sleep(1)
