# My notes on the first part of the course

from robot_control_class import RobotControl
# here i importing Class called RobotControl
# import allows you to use the class in your code from other modueles.
# This means that the Python code in your program can execute the Python code defined in another program file (in this case, the code of the RobotControl class), without having to rewrite it.

# ** IN GENERAL **
# To import the code of another Python module, indicate the following:
# from <name_of_the_module> import <method_or_class_to_be_imported>

rc = RobotControl()
# here we are creating variable called rc


a = rc.get_laser(360)
# here we are calling method of class 
# get_laser is a method of class RobotControl
# 360 is a parameter of method get_laser in front of the robot
# values from 0 to 719 represent the laser beams direction angles start 0 from right to 719 to left
# a is a variable that will store the value returned by the method get_laser

print ("The distance measured is: ", a)
# here we are printing the value of variable a

# the output will print the distance measured by the laser sensor in front of the robot from the center of the robot to the wall in front of it.