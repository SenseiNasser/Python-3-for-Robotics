from robot_control_class import RobotControl


num = int(input("Select a number between 0 and 719: ")) 
# creating variable called num
# ask user to input a number between 0 and 719 and it will save user input value in num
# user will type number represent the angle



rc = RobotControl()
# creating variable rc represent RobotControl Class

a = rc.get_laser(num)
# Creating variable a 
# Calling method from Class rc

print ("The laser value received is: ", a)
