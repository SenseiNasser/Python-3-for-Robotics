from robot_control_class import RobotControl

robotcontrol = RobotControl()

a = robotcontrol.get_laser(360)
# a variable to store the laser reading distance to the wall in front of the robot (360 degrees)

# while the distance to the wall is greater than 1 meter, move the robot forward
# and update the distance to the wall
# when the distance to the wall is equal or less than 1 meter, stop the robot
while a > 1:
    robotcontrol.move_straight()
    a = robotcontrol.get_laser(360)
    print ("Current distance to wall: %f" % a)

robotcontrol.stop_robot()

print ("Wall is at %f meters! Stop the robot!" % a)
# %f is a placeholder for a floating point number
# the output will be something like: Wall is at 0.500000 meters! Stop the robot!