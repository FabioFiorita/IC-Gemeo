from robodk.robolink import *      # RoboDK's API
from robodk.robomath import *      # Math toolbox for robots
from robodk.robodialogs import *      # Basic dialog boxes

RL = Robolink()

robot = RL.Item('KUKA KR 6 R900 sixx')

app_InspectA = RL.Item('App_InspectA')
retract_InspectA = RL.Item('Retract_InspectA')

def moveRobot(shape):
    robot.MoveJ(app_InspectA)
    if shape == 3:
        moveTriangle()
    else:
        moveSquare()
    robot.MoveJ(retract_InspectA)
    
def moveTriangle():
    for i in range(1, 4):
        targetName = f"Triangle {i}"
        robot.MoveJ(RL.Item(targetName))
    robot.MoveJ(RL.Item("Triangle 1"))

def moveSquare():
    for i in range(1, 5):
        targetName = f"Square {i}"
        robot.MoveJ(RL.Item(targetName))
    robot.MoveJ(RL.Item("Square 1"))

shape = mbox('Select shape:', entry=True)
shape = int(shape)
moveRobot(shape)
