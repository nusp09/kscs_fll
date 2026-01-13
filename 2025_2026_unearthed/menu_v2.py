from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, Matrix, run_task, multitask

# -------------------- HUB SETUP --------------------
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub.display.orientation(up=Side.LEFT)
hub.speaker.volume(100)
hub.system.set_stop_button(Button.BLUETOOTH)
# -------------------- MOTORS --------------------
driveL = Motor(Port.A, Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.B)
AttachmentL = Motor(Port.C)
AttachmentR = Motor(Port.D)

base = DriveBase(driveL, driveR, wheel_diameter=62.4, axle_track=111)
base.use_gyro(True)

# -------------------- GLOBAL STOP FLAG --------------------
stop_requested = False

# -------------------- STOP MONITOR --------------------
async def stop_monitor():
    global stop_requested
    while not stop_requested:
        if Button.CENTER in hub.buttons.pressed():
            stop_requested = True
            base.stop()
            driveL.stop()
            driveR.stop()
            AttachmentL.stop()
            AttachmentR.stop()
        await wait(20)

# -------------------- SAFE HELPERS --------------------
async def safe_straight(dist):
    if stop_requested: return
    await base.straight(dist)

async def safe_turn(angle):
    if stop_requested: return
    await base.turn(angle)

async def safe_run_angle(motor, speed, angle):
    if stop_requested: return
    await motor.run_angle(speed, angle)

# -------------------- MISSIONS --------------------
async def india_jones():
    global stop_requested
    stop_requested = False

    await safe_straight(750)
    await safe_straight(-100)
    await safe_run_angle(AttachmentL, 1000, -720)
    await safe_straight(175)
    await safe_turn(75)
    await safe_straight(62.5)
    await safe_run_angle(AttachmentL, 1000, 720)
    await safe_turn(15)
    await safe_straight(300)
    await safe_run_angle(AttachmentL, 1000, -1080)
    await safe_run_angle(AttachmentL, 1000, 1080)
    await safe_straight(-200)

async def boat():
    global stop_requested
    stop_requested = False

    await safe_straight(570)
    await safe_run_angle(AttachmentR, 500, -270)
    await safe_straight(-75)
    await safe_run_angle(AttachmentR, 500, 270)
    await safe_turn(-90)
    await safe_straight(110)
    await safe_turn(90)
    await safe_straight(1000)

async def scales():
    global stop_requested
    stop_requested = False

    await safe_straight(750)
    await safe_turn(90)
    await safe_straight(180)
    await safe_straight(-150)

async def red_beam():
    global stop_requested
    stop_requested = False

    await safe_straight(410)
    await safe_turn(-45)
    await safe_straight(73)
    await safe_run_angle(AttachmentL, 500, -360)
    await safe_turn(-20)
    await safe_turn(20)
    await safe_straight(-400)
    await safe_run_angle(AttachmentL, 500, 360)

async def boulders():
    global stop_requested
    stop_requested = False

    await safe_straight(785)
    await safe_turn(45)
    await safe_straight(35)
    await safe_run_angle(AttachmentL, 500, -360)
    await safe_run_angle(AttachmentL, 500, 360)
    await safe_turn(90)
    await safe_straight(-280)

async def arm():
    global stop_requested
    stop_requested = False

    await safe_straight(460)
    for _ in range(3):
        await safe_run_angle(AttachmentR, 2000, -50)
        await safe_run_angle(AttachmentL, 2000, 50)
        await safe_run_angle(AttachmentR, 2000, 50)
        await safe_run_angle(AttachmentL, 2000, -50)
    await safe_straight(-460)

# -------------------- MISSION PICKER --------------------
def picker(num):
    if num == 1:
        run_task(multitask(india_jones(), stop_monitor()))
    elif num == 2:
        run_task(multitask(boat(), stop_monitor()))
    elif num == 3:
        run_task(multitask(scales(), stop_monitor()))
    elif num == 4:
        run_task(multitask(red_beam(), stop_monitor()))
    elif num == 5:
        run_task(multitask(boulders(), stop_monitor()))
    elif num == 6:
        run_task(multitask(arm(), stop_monitor()))

# -------------------- MENU ICONS --------------------
nums = [
    Matrix([[1,1,1,0,0],[1,0,1,0,0],[1,0,1,0,0],[1,0,1,0,0],[1,1,1,0,0]])*100,
    Matrix([[0,1,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[1,1,1,0,0]])*100,
    Matrix([[1,1,1,0,0],[0,0,1,0,0],[1,1,1,0,0],[1,0,0,0,0],[1,1,1,0,0]])*100,
    Matrix([[1,1,1,0,0],[0,0,1,0,0],[1,1,1,0,0],[0,0,1,0,0],[1,1,1,0,0]])*100,
    Matrix([[1,0,1,0,0],[1,0,1,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])*100,
    Matrix([[1,1,1,0,0],[1,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[1,1,1,0,0]])*100,
    Matrix([[1,1,1,0,0],[1,0,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[1,1,1,0,0]])*100,
]

# -------------------- MENU LOOP --------------------
program = 1
upper_bound = 6
lower_bound = 1

hub.display.icon(nums[program])

while True:
    buttons = hub.buttons.pressed()

    if buttons == {Button.LEFT}:
        program -= 1
        if program < lower_bound:
            program = upper_bound
        hub.display.icon(nums[program])
        wait(200)

    if buttons == {Button.RIGHT}:
        program += 1
        if program > upper_bound:
            program = lower_bound
        hub.display.icon(nums[program])
        wait(200)

    if buttons == {Button.CENTER}:
        while Button.CENTER in hub.buttons.pressed():
            wait(10)
        picker(program)
        wait(500)
    wait(50)
