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
async def move_arm():
    await AttachmentR.run_angle(500,-180)
async def main():
    await base.straight(830)
    await base.turn(90)
    await base.straight(900)
    await base.turn(45)
    base.straight(150)
    await wait(200)
    await AttachmentR.run_angle(500,180)
    await base.straight(-150)
    await base.turn(-45)
    await multitask(base.straight(360),move_arm())
    await base.turn(70)
    await base.straight(740)
run_task(main())
