    """
    this SHOULD get the angles from the current limb positions and print it to the ROS command line

    """
import argparse
import sys
import math
import rospy

from baxter_interface import (
    DigitalIO,
    Gripper,
    Navigator,
    CHECK_VERSION,
)


Llimb = baxter_interface.Limb('left')
Langles = Llimb.joint_angles()

Rlimb = baxter_interface.Limb('right')
Rangles = Rlimb.joint_angles()

print Langles
print Rangles
