from robot_control_class import RobotControl
import time
# import RobotControl class from robot control class module
# time is a library that allows us to use the sleep function


# create an object called robotcontrol 
robotcontrol = RobotControl(robot_name="summit")


# function to move the robot forward for a given number of seconds
# note that the robot will move forward until the time is up, even if it hits an obstacle
# robotcontrol.move_straight() starts the robot moving forward
# time.sleep(secs) pauses the program for the given number of seconds
# robotcontrol.stop_robot() stops the robot
def move_x_seconds(secs):
    robotcontrol.move_straight()
    time.sleep(secs)
    robotcontrol.stop_robot()

# call the function to move the robot forward for 5 seconds
move_x_seconds(5)