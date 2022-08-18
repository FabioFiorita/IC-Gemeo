from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
from graphic_interface import interface

RL = Robolink()

robot = RL.Item('Robot')
base = RL.Item('Base')
inspect = RL.Item('Inspect')
retract = RL.Item('Retract')

target = RL.AddTarget('Cube', base)
center = interface()
RL.ShowMessage('Centers: ' + str(center))
target.setPose(Offset(eye(), 600, -100, 0, -180, 0, 180))

robot.MoveJ(inspect)
robot.MoveJ(target)
robot.MoveJ(retract)