#start at the first line of the program 
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix, run_task, multitask, hub_menu
# all angles are relative
motor_limits = [1000, 2000, 200]
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
#####
selected = hub_menu("1", "2", "3", "4", "5", "6")

def init():
    #use this to reduce motor backlash and gyro issues
    base.reset()
    base.straight(-15)
def outing1():
    base.straight(700)
    base.straight(-120)
    base.straight(50)
    AttachmentL.run_angle(300,270)#picks up brush after swiping it
    base.turn(45)
    base.straight(175)
    base.turn(-90)
    base.straight(180)
    AttachmentR.run_angle(300,60)#picks up topsoil
    base.straight(-50)
    base.straight(60)#push forwards again to ensure all soil is uncovered
    base.straight(-120)
    base.turn(45)
    base.straight(-800)
    AttachmentL.run_angle(300,-270)
def outing2():
    right_angle = 360*11#set how to do a 90 degree turn with the screw gear
    base.straight(730)
    AttachmentR.run_angle(1000,-right_angle)#puts arm down
    AttachmentL.run_angle(1000,-right_angle*1.1)#turns the end gears
    AttachmentR.run_angle(1000,right_angle)
    base.straight(-720)
def outing3():
    #first introduction to asynchronous functions: an async function allows proscesses to be run inline with each other such as putting the arm down and moving forwards or putting it back up on a long straight section it alows us to run multiple motors at once with the main use for driving and moving motors
    async def move_arm():
        await AttachmentR.run_angle(500,-180)#puts the arm up
    async def outing_3():
        await base.straight(830)
        await base.turn(90)
        await base.straight(900)#this is where it pushes over the cart
        await base.turn(45)
        base.straight(150)
        await wait(200)
        await AttachmentR.run_angle(500,180)#completes raise the roof and tip the scale
        await base.straight(-150)
        await base.turn(-45)
        await multitask(base.straight(360),move_arm())#pulls attachment arm in whilst moving to avoid excess time loss
        await base.turn(70)
        await base.straight(740)
    run_task(outing_3())
def outing4():
    base.straight(470)
    #we use a for loop here to avoid repeating code unnessicarily
    for i in range(3):
        AttachmentR.run_angle(500,-180,Stop.HOLD, False)#neat little trick to move a motor for an ammount of time instead of an angle is to set the wait parameter to False
        wait(500)
        AttachmentR.run_angle(200,140)#empties silo
    base.straight(-170)
    AttachmentR.run_angle(250,-180,Stop.HOLD, False)
    wait(500)
    base.turn(-55)#completes market stall
    base.straight(120)
    base.turn(-45)
    AttachmentR.run_angle(250,180)
    base.straight(210)
    base.turn(30)
    AttachmentR.run_angle(250,-180)
    for i in range(5):
        base.turn(-9)
        base.straight(-5)
    base.turn(-9)
    base.turn(-9)
    base.turn(50)#pulls the pan out
    base.straight(-450)
    base.turn(-90)
def outing5():
    #our best use of the async function is this outing we used a function called frint rack and arm to control the two attachments and a main proscess to call these functions from
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
        await front_rack('right')#completes the who lived here 
        await base.straight(-50)
        await multitask(base.turn(-90),front_rack('left center'))
        await multitask(base.straight(-230),arm('down'))
        await base.straight(-80)#picks up the heavy lifting
        await arm('up')
        await base.straight(300)
        await base.turn(-90)
        await multitask(base.straight(700),front_rack('left'))
    run_task(outing_5())
def outing6():
    base.straight(680)
    base.turn(25)
    base.straight(400)
    AttachmentR.run_angle(500,320)#completes statue rebuilt
    base.straight(-200)
    base.turn(65)
    base.straight(500)
    base.turn(-90)
    base.straight(380)
    base.turn(-90)
    base.straight(40)
    AttachmentL.run_angle(500,200)#dumps all of the thingies in the forum
    AttachmentL.run_angle(500,-200)
    AttachmentL.run_angle(500,200)
    base.straight(-50)
    base.turn(-90)
    base.straight(-180)#finishes with the sand castle in the spot 
######
#menu to select the outings
if selected == "1":
    init()
    outing1()
elif selected == "2":
    base.reset()
    outing2()
elif selected == "3":
    init()
    outing3()
elif selected == "4":
    init()
    outing4()
elif selected == "5":
    init()
    outing5()
elif selected == "6":
    base.reset()
    outing6()
