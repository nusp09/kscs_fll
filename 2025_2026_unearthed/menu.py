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
hub.system.set_stop_button(Button.BLUETOOTH)

driveL = Motor(Port.A, Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.B)
AttachmentL = Motor(Port.C)
AttachmentR = Motor(Port.D)
SensorL = ColorSensor(Port.E)
SensorR = ColorSensor(Port.F)
base = DriveBase(driveL, driveR, wheel_diameter=62.4, axle_track=111)
base.use_gyro(True)
####
#selected = hub_menu("1", "2", "3", "4", "5", "6")

async def india_jones():
    base.straight(750)
    base.straight(-100)
    AttachmentL.run_angle(1000,-720)
    base.straight(175)
    base.turn(75)
    base.straight(62.5)
    AttachmentL.run_angle(1000,720)
    base.turn(15)
    base.straight(300)
    AttachmentL.run_angle(1000,-1080)
    AttachmentL.run_angle(1000,1080)
    base.straight(-200)
    base.turn(235)
    base.straight(100)
    base.turn(35)
    AttachmentL.run_angle(1000,-720)
    base.straight(-850)
    AttachmentL.run_angle(1000,720)
async def boat():
    base.straight(570)
    AttachmentR.run_angle(500, -270)
    base.straight(-75)
    AttachmentR.run_angle(500, 270)
    base.turn(-90)
    base.straight(110)
    base.turn(90)
    base.straight(280)
    base.straight(-50)
    base.turn(-45)
    base.straight(120)
    base.turn(45)
    base.straight(1000)
async def scales():
    base.straight(750)
    base.turn(90)
    base.straight(180)
    base.straight(-150,Stop.HOLD,False)
    wait(500)
    base.straight(-30)
    base.straight(30)
    base.straight(-100)
    base.turn(90)
    base.straight(650)
async def red_beam():
    base.straight(410)
    base.turn(-45)
    base.straight(73)
    AttachmentL.run_angle(500, -360)
    base.turn(-20)
    base.turn(20)
    base.straight(-400)
    AttachmentL.run_angle(500, 360)
async def boulders():
    base.straight(785)
    base.turn(45)
    base.straight(35)
    AttachmentL.run_angle(500,-360)
    AttachmentL.run_angle(500,360)
    base.straight(-25)
    base.turn(-45)
    base.straight(30)
    AttachmentL.run_angle(500,-360)
    AttachmentL.run_angle(500,360)
    base.turn(90)
    base.straight(-280)
    base.turn(-125)
    base.straight(-1000,Stop.HOLD,False)
    wait(6700)
    
    base.straight(90)
    base.turn(-50)
    base.straight(-200)
    base.turn(50)
    base.straight(-650)
async def arm():
    base.straight(460)
    angle = 50 
    for i in range(0,3):
        AttachmentR.run_angle(2000,-angle,Stop.HOLD,False)
        AttachmentL.run_angle(2000,angle,Stop.HOLD)
        AttachmentR.run_angle(2000,angle,Stop.HOLD,False)
        AttachmentL.run_angle(2000,-angle,Stop.HOLD)
    base.straight(-460)
battery = [Matrix([
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ]

        )*100,
Matrix([
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ]

        )*100,
Matrix([
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ]

        )*100,
           ]
# Based on the selection, run a program.
#if selected == "1":
   #india_jones()      
#elif selected == "2":
   #boat() 
#elif selected == "3":
   #scales()
#elif selected == "4":
   #red_beam()
#elif selected == "5":
   #boulders()
#elif selected == "6":
    #arm()
loop_delay = 50
upper_bound = 6
lower_bound = 1
program = 1
#hub.imu.ready()

nums = [

        Matrix([
            [1, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            ]

               )*100,
        Matrix([
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            ]

               )*100,
        ]
ready = Matrix([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            ])*100
async def picker(num):
    if num == 1:
        india_jones()
    elif num == 2:
        boat()
    elif mum == 3:
        scales()
    elif num == 4:
        red_beam()
    elif num == 5:
        boulders()
    elif num == 6:
        arm()
async def check_stop():
    base.stop()
    driveL.stop()
    driveR.stop()
    AttachmentL.stop()
    AttachmentR.stop()
hub.display.icon(nums[program]+ready)
def menu_loop(program,loop_delay):
    selected = 1
    while True:
        if hub.imu.ready() == True:
            ready = Matrix([
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                ])*100
        else:
            ready = Matrix([
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                ])*100
        button = hub.buttons.pressed()
        if button == {Button.LEFT}:
            program -= 1
            if program < 1:
                program = upper_bound
            hub.display.icon(nums[program]+ready)
            wait(100)
        if button == {Button.RIGHT}:
            program += 1
            if program > 6:
                program = lower_bound
            hub.display.icon(nums[program]+ready)
            wait(150)
        if button == {Button.CENTER}:
            selected += 1
            if selected%2 == 0:
                picker(program)
            else:
                check_stop()
        wait(loop_delay)
menu_loop(program,loop_delay)
