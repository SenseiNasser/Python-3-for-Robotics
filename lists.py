from robot_control_class import RobotControl
# importing the class RobotControl from the robot control class module

rc = RobotControl()
# creating variable rc and assigning it to the class RobotControl

l = rc.get_laser_full()
# creating variable l and assigning it to the function get_laser_full from the class RobotControl
# the function get_laser_full returns a list of 720 values
# each value represents the distance to an object in front of the robot
# note that the list is indexed from 0 to 719
# note that the robot has a laser scanner that scans 360 degrees in front of the robot

print ("Position 0: ", l[0])
# printing the value at position 0 in the list l
# note that the value at position 0 is the distance to an object directly in right of the robot
print ("Position 360: ", l[360])
# printing the value at position 360 in the list l
# note that the value at position 360 is the distance to an object directly in front of the robot
print ("Position 719: ", l[719])
# printing the value at position 719 in the list l
# note that the value at position 719 is the distance to an object directly in left of the robot