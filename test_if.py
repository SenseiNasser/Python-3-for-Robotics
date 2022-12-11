from robot_control_class import RobotControl


robotcontrol = RobotControl() 
# create variable robotcontrol and assign it to the class RobotControl

a = robotcontrol.get_laser(360)
# create variable a and assign it to the value of the laser reading
# 360 is the angle of the laser reading
# meaning that the laser reading is taken from the front of the robot

# if the laser reading is less than 1 meter from the wall, the robot stops
# otherwise, the robot moves forward
if a < 1:
    robotcontrol.stop_robot()

else:
    robotcontrol.move_straight()

# print the value of the laser reading
print ("The laser value received was: ", a)
