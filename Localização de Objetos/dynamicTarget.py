from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots

RL = Robolink()

robot = RL.Item('Robot')
base = RL.Item('Base')
inspect = RL.Item('Inspect')
retract = RL.Item('Retract')

target = RL.AddTarget('Cube', base)
target.setPose(Offset(eye(), 600, -100, 0, -180, 0, 180))

robot.MoveJ(inspect)
robot.MoveJ(target)
robot.MoveJ(retract)