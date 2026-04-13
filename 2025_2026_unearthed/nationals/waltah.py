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
selected = hub_menu("1", "2", "3", "4", "5", "6")

def outing1():
    base.straight(700)
    base.straight(-120)
    base.straight(50)
    AttachmentL.run_angle(300,270)
    base.turn(45)
    base.straight(175)
    base.turn(-90)
    base.straight(180)
    AttachmentR.run_angle(300,60)
    base.straight(-50)
    base.straight(60)
    base.straight(-120)
    base.turn(45)
    base.straight(-800)
    AttachmentL.run_angle(300,-270)
def outing2():
    right_angle = 360*10
    base.straight(750)
    AttachmentR.run_angle(1000,-right_angle)
    AttachmentL.run_angle(1000,-right_angle)
    AttachmentR.run_angle(1000,right_angle)
    base.straight(-750)
def outing3():
    async def move_arm():
        await AttachmentR.run_angle(500,-180)
    async def outing_3():
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
    run_task(outing_3())
def outing4():
    base.straight(470)
    for i in range(3):
        AttachmentR.run_angle(500,-180,Stop.HOLD, False)
        wait(500)
        AttachmentR.run_angle(200,140)
    base.straight(-170)
    AttachmentR.run_angle(250,-180,Stop.HOLD, False)
    wait(500)
    base.turn(-55)
    base.straight(120)
    base.turn(-45)
    AttachmentR.run_angle(250,180)
    base.straight(200)
    base.turn(25)
    AttachmentR.run_angle(250,-180)
    base.turn(-9)
    base.turn(-9)
    base.turn(-9)
    base.turn(-9)
    base.turn(-9)
    base.turn(-9)
    base.turn(-9)
    base.turn(50)
    base.straight(-450)
    base.turn(-90)
def outing5():
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
    
    
    
    async def outing_5():
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
    run_task(outing_5)
def outing6():
    base.straight(700)
    base.turn(20)
    base.straight(400)
    AttachmentR.run_angle(500,320)
    base.straight(-200)
    base.turn(70)
    base.straight(500)
    base.turn(-90)
    base.straight(380)
    base.turn(-90)
    base.straight(40)
    AttachmentL.run_angle(500,200)
    AttachmentL.run_angle(500,-200)
    AttachmentL.run_angle(500,200)
    AttachmentL.run_angle(500,-200)
    base.straight(-50)
    base.turn(-90)
    base.straight(-180)

if selected == "1":
    outing1()
elif selected == "2":
    outing2()
elif selected == "3":
    outing3()
elif selected == "4":
    outing4()
elif selected == "5":
    outing5()
elif selected == "6":
    outing6()

