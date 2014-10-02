    """
    this prints the angles (first from the left arm, then the right one)

    """
import argparse
import sys
import rospy

from baxter_interface import (
    DigitalIO,
)


Llimb = baxter_interface.Limb('left')
Langles = Llimb.joint_angles()

Rlimb = baxter_interface.Limb('right')
Rangles = Rlimb.joint_angles()

print "showing left angles"
print Langles
print "showing right angles"
print Rangles
