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

def turn(angle):
    integral = 0
    loop_delay = 5  
    target = hub.imu.heading()+angle
    previous_error = 0
    error = target - hub.imu.heading()
    while error > 0.5 or error < -0.5:
        error = target - hub.imu.heading()
        kp = 0.75
        ki = 0.0001
        kd = 0.25 
        proportional = error*kp
        integral += error * ki
        derivative = ((error-previous_error) / 0.05)*kd
        output = proportional + integral + derivative 
        previous_error = error
        print('p = ', proportional)
        print('i = ', integral)
        print('d = ', derivative)
        print(output)
        print(error)
        base.turn(output, wait=False)
        wait(loop_delay)
        
while True:
    turn(90)

