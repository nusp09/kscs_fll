from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix
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
drive = DriveBase(driveL, driveR, wheel_diameter=62.4, axle_track=111)
drive.use_gyro(True)

hub.speaker.play_notes(["D4/4", "F4/4", "F4/8_", "G4/8", "G4/4", "Bb4/16_", "A4/16", "Bb4/16_", "A4/16", "Bb4/16_", "A4/16", "F4/8", "F4/8", "G4/8", "G4/4" ], 80)

hub.speaker.play_notes(["D4/4", "F4/4", "F4/8_", "G4/8", "G4/4", "Bb4/16_", "A4/16", "Bb4/16_", "A4/16", "Bb4/16_", "A4/16", "F4/8", "F4/8", "G4/8", "G4/4" ], 80)

