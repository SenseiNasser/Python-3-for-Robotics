from robot_control_class import RobotControl
# importing the class RobotControl from the robot control class module

robotcontrol = RobotControl()
# creating variable robotcontrol and assigning it to the class RobotControl

laser1 = robotcontrol.get_laser(0)
print ("The laser value received is: ", laser1)
# creating variable laser1 and assigning it to the function get_laser from the class RobotControl
# printing the laser value received
# 0 value means to right of the robot

laser2 = robotcontrol.get_laser(360)
print ("The laser value received is: ", laser2)
# creating variable laser2 and assigning it to the function get_laser from the class RobotControl
# printing the laser value received
# 360 value means to front of the robot

laser2 = robotcontrol.get_laser(719)
print ("The laser value received is: ", laser2)
# creating variable laser2 and assigning it to the function get_laser from the class RobotControl
# printing the laser value received
# 719 value means to left of the robot