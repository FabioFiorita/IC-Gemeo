from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots

RL = Robolink()

robot = RL.Item('KUKA KR 6 R900 sixx')

target1 = RL.Item('Target 1')
target2 = RL.Item('Target 2')
target3 = RL.Item('Target 3')
target4 = RL.Item('Target 4')

robot.MoveJ(target1)
robot.MoveJ(target2)
robot.MoveJ(target3)
robot.MoveJ(target4)
robot.MoveJ(target1)

