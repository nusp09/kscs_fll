#start at the first line of the program
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix, run_task, multitask
# all angles are relative
motor_limits = [1000, 2000, 200]
hub = PrimeHub()
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub.display.orientation(up=Side.LEFT)
hub.speaker.volume(100)

driveL = Motor(Port.A, Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.B)
AttachmentL = Motor(Port.C)
AttachmentR = Motor(Port.D)
SensorL = ColorSensor(Port.E)
SensorR = ColorSensor(Port.F)
base = DriveBase(driveL, driveR, wheel_diameter=62.4, axle_track=111)
base.use_gyro(True)
#####
base.straight(750)
base.turn(90)
base.straight(180)
base.straight(-150,Stop.HOLD,False)
wait(500)
base.turn(-150,Stop.HOLD,False)
wait(1000)
for i in range(0,3):
    base.turn(90,Stop.HOLD,False)
    wait(1000)
    base.turn(-90,Stop.HOLD,False)
    wait(1100)
base.turn(260)
base.straight(650)
