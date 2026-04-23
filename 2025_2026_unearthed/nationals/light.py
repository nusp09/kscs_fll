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

# Speed
def line_square():
    LINE_THRESHOLD = 20 
    SPEED = 200
    left_done = False
    right_done = False
    for i in range(5):  
        while not (left_done and right_done):
            left_reflection = SensorL.reflection()
            right_reflection = SensorR.reflection()
    
            # Left side
            if not left_done:
                if left_reflection < LINE_THRESHOLD:
                    driveL.stop()
                    left_done = True
                else:
                    driveL.run(SPEED)
    
            # Right side
            if not right_done:
                if right_reflection < LINE_THRESHOLD:
                    driveR.stop()
                    right_done = True
                else:
                    driveR.run(SPEED)
    
            wait(10)
        SPEED = SPEED/2
        left_done = False
        right_done = False
        base.straight(-10)

    # Ensure both motors are stopped
line_square()
