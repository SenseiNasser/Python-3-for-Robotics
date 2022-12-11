from robot_control_class import RobotControl

rc = RobotControl()

l = rc.get_laser_full()
# create a list of 719 elements representing the laser readings

# dictionary with the laser readings from the 8 angle points
dict = {"P0": l[0], "P100": l[100], "P200": l[200], "P300": l[300], "P400": l[400], "P500": l[500], "P600": l[600], "P719": l[719]}
# for the 8 angle points, the keys are P0, P100, P200, P300, P400, P500, P600, P719


print (dict)

# the output will be :
# {'P0': inf, 'P100': inf, 'P200': inf, 'P300': 2.5677835941314697, 'P400': 2.541300058364868, 'P500': inf, 'P600': inf, 'P719': inf}
# inf meaning no obstacle in that angle