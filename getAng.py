#!/usr/bin/env python
"""
this  grabs the angles of the arms and head (given the correct arguments)
It then prints them to the command line
"""
import argparse
import sys
import math
import rospy
import  baxter_interface
from std_msgs.msg import String
rospy.init_node('angles', anonymous=True)

def getInfo(limb, head):
	if limb == 'left' or limb == 'both':
		Llimb = baxter_interface.Limb('left')
		Langles = Llimb.joint_angles()
		print Langles

	if limb == 'right' or limb == 'both':
		Rlimb = baxter_interface.Limb('right')
		Rangles = Rlimb.joint_angles()
		print Rangles

	if head:
		head = baxter_interface.Head()
		print 'Head angle: ' head.pan()
		if head.nodding():
			print 'Baxter is nodding :D'
		else:
			print 'not nodding :('


def main():
	arg_fmt = argparse.RawDescriptionHelpFormatter
	parser = argparse.ArgumentParser(formatter_class=arg_fmt, description=main.__doc__)

	parser.add_argument('-a', '--arm', dest='arm', default='both',
		choices=['both', 'left', 'right'],
		help='arm to get data from (default: both)')
	parser.add_argument('-h', '--head', dest='head',
		action='store_true',
		help='also show head data')


	args = parser.parse_args(rospy.myargv()[1:])

	getInfo(args.arm,args.head)

if __name__ == '__main__':
    main()
