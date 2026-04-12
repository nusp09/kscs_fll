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
async def front_rack(direction):
    if direction == 'left':
        await AttachmentL.run_angle(700,400)
    if direction == 'right':
        await AttachmentL.run_angle(700,-400)
    if direction == 'right center':
        await AttachmentL.run_angle(700,-250)
    if direction == 'left center':
        await AttachmentL.run_angle(700,250)

async def arm(direction):
    if direction == 'up':
        await AttachmentR.run_angle(150,-180)
    if direction == 'down':
        await AttachmentR.run_angle(100,200)



async def main():
    await base.straight(800)
    await front_rack('left')
    await front_rack('right')
    await base.straight(-50)
    await multitask(base.turn(-90),front_rack('left center'))
    await multitask(base.straight(-230),arm('down'))
    await base.straight(-80)
    await arm('up')
    await base.straight(300)
    await base.turn(-90)
    await multitask(base.straight(700),front_rack('left'))

    
run_task(main())

