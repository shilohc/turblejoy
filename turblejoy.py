#!/usr/bin/env python
import roslib; roslib.load_manifest('missile_launcher')
import rospy
from std_msgs.msg import String
#from missile_launcher.msg import missile_cmd
#import missile_launcher.msg 
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
#import missile_launcher
from missile_launcher.msg import yak_cmd

msg_root = "/home/shiloh/devel/audio_assets/"

# TUNING CONSTANTS #
joytune = rospy.get_param('joytune', [2.0, 2.0])
#Linear factor
lscale = joytune[0]
#Angular scale
ascale = joytune[1]

def repub_twist(event):
    pubt.publish(twist)

def missile_translator(data):
    #print data
    if data.buttons[0] == 1:
        pub.publish(String("f"))
    elif data.buttons[1] == 1:
        pub.publish(String("d"))
    elif data.buttons[2] == 1:
        pub.publish(String("u"))
    elif data.buttons[3] == 1:
        pub.publish(String("l"))
    elif data.buttons[4] == 1:
        pub.publish(String("r"))
    elif data.buttons[5] == 1:
        pub.publish(String("h"))
    else:
        pub.publish(String("s"))

    if data.buttons[7] == 1:
        yak.cmd = "wav"
        yak.param = "turble_engarde_2.wav"
        pubs.publish(yak)
    if data.buttons[8] == 1:
        yak.cmd = "wav"
        yak.param = "turble_activate-missile-launcher-kowalski.wav"
        pubs.publish(yak)
    
    twist.linear.x = data.axes[1]
    twist.angular.z = data.axes[0]
    pubt.publish(twist)

def joy_init():
    global twist
    twist = Twist()
    global yak
    yak = yak_cmd()
    rospy.init_node('turblejoy', anonymous=True)
    rospy.Subscriber("joy", Joy, missile_translator)
    global pub
    global pubt
    global pubs
    pub = rospy.Publisher('missile_launcher', String)
    pubt = rospy.Publisher('cmd_vel', Twist)
    pubs = rospy.Publisher('yak', yak_cmd)
    rospy.Timer(rospy.Duration(0.5), repub_twist)
    rospy.spin()

if __name__ == '__main__':
    joy_init()