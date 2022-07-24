from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots

RL = Robolink()

robot = RL.Item('UR10e')

app_InspectA = RL.Item('App_InspectA')
retract_InspectA = RL.Item('Retract_InspectA')

def moveRobot():
    robot.MoveL(app_InspectA)
    moveTargets(8)
    robot.MoveL(retract_InspectA)
    
def moveTargets(targets):
    for i in range(1, targets):
        targetName = f"InspectA {i}"
        robot.MoveJ(RL.Item(targetName))

moveRobot()
