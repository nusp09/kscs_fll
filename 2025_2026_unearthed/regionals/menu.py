#start at the first line of the program
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix, run_task, multitask, hub_menu
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
selected = hub_menu("1", "2", "3", "4", "5", "6")

def india_jones():
    base.straight(750)
    base.straight(-110)
    AttachmentL.run_angle(1000,-720)
    base.straight(-200)
    base.straight(380)
    base.turn(75)
    base.straight(65)
    AttachmentL.run_angle(1000,720)
    base.turn(15)
    base.straight(300)
    AttachmentL.run_angle(1000,-1080)
    base.straight(-200)
    AttachmentL.run_angle(1000,1080)
    base.turn(230)
    base.straight(110)
    base.turn(35)
    AttachmentL.run_angle(1000,-720)
    base.straight(-850)
    AttachmentL.run_angle(1000,720)
def boat():
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
def scales():
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
def red_beam():
    base.straight(410)
    base.turn(-45)
    base.straight(72)
    AttachmentL.run_angle(500, -360)
    base.turn(-20)
    base.turn(20)
    base.straight(-400)
    AttachmentL.run_angle(500, 360)
def boulders():
    base.straight(783)
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
    wait(3200)
    
    base.straight(90)
    base.turn(-50)
    base.straight(-200)
    base.turn(60)
    base.straight(-650)
def arm():
    base.straight(460)
    angle = 70 
    for i in range(0,3):
        AttachmentR.run_angle(500,-angle,Stop.HOLD,False)
        AttachmentL.run_angle(500,angle,Stop.HOLD)
        AttachmentR.run_angle(500,angle,Stop.HOLD,False)
        AttachmentL.run_angle(500,-angle,Stop.HOLD)
    base.straight(-460)
# Based on the selection, run a program.
if selected == "1":
   india_jones()      
elif selected == "2":
   boat() 
elif selected == "3":
   scales()
elif selected == "4":
   red_beam()
elif selected == "5":
   boulders()
elif selected == "6":
    arm() 

