from robot_control_class import RobotControl

robotcontrol = RobotControl()

l = robotcontrol.get_laser_full()
# l is a list with 719 values, one for each degree
# values represent the laser beam distance in meters


maxim = 0
# maxim represents the maximum value in the list
# we start with 0
# we will compare each value in the list with maxim
# if the value is higher than maxim, we will update maxim
# at the end, maxim will contain the highest value in the list
for value in l:
    if value > maxim:
        maxim = value

# print the highest value in the list
print ("The higher value in the list is: ", maxim)
