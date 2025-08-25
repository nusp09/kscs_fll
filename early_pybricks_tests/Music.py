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
drive = DriveBase(driveL, driveR, wheel_diameter=62.4, axle_track=111)
drive.use_gyro(True)

bpm = 200 

ThroughTheFireAndFlames = ["C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "G4/8", "Eb4/8", "F4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Bb3/8",
                           "C4/8", "D4/8", "Eb4/8", "C4/8", "D4/8", "Eb4/8", "F4/8", "D4/8",
                           "Bb4/16", "F4/16", "Eb4/16", "C4/16", "Bb3/16", "C4/16", "Eb4/16", "F4/16", "Bb4/16", "G4/16", "C5/16", "Bb4/16", "G4/16", "F4/16", "Eb4/16", "F4/16"
                           "Eb5/16", "Eb5/16", "Eb5/16", "Eb5/16", "C5/16", "C5/16", "Eb5/16", "Eb5/16", "Eb5/16", "Eb5/16", "C5/16", "C5/16", "Eb5/16", "Eb5/16", "C5/16", "C5/16",
                           "Eb5/16", "Eb5/16", "Eb5/16", "Eb5/16", "C5/16", "C5/16", "Eb5/16", "Eb5/16", "Eb5/16", "Eb5/16", "C5/16", "C5/16", "Eb5/16", "Eb5/16", "C5/16", "C5/16"
                           "G5/16", "G5/16", "G5/16", "G5/16", "C5/16", "C5/16", "G5/16", "G5/16", "G5/16", "G5/16", "C5/16", "C5/16", "G5/16", "G5/16", "C5/16", "C5/16", 
                           "G5/16", "G5/16", "G5/16", "G5/16", "C5/16", "C5/16", "G5/16", "G5/16", "G5/16", "G5/16", "C5/16", "C5/16", "G5/16", "G5/16", "C5/16", "C5/16", 
                           "F5/16", "F5/16", "F5/16", "F5/16", "C5/16", "C5/16", "F5/16", "F5/16", "F5/16", "F5/16", "C5/16", "C5/16", "F5/16", "F5/16", "C5/16", "C5/16", 
                           "F5/16", "F5/16", "F5/16", "F5/16", "C5/16", "C5/16", "F5/16", "F5/16", "F5/16", "F5/16", "C5/16", "C5/16", "F5/16", "F5/16", "C5/16", "C5/16", 
"Eb5/16", "Eb5/16", "Eb5/16", "Eb5/16", "G4/16", "G4/16", "Eb5/16", "Eb5/16", "Eb5/16", "Eb5/16", "G4/16", "G4/16", "Eb5/16", "Eb5/16", "G4/16", "G4/16", 
                           "D5/16", "B4/16", "Ab4/16", "B4/16", "G4/16", "B4/16", "D5/16", "Eb5/16", "F5/16", "Eb5/16", "F5/16", "G5/16", "F5/16", "Eb5/16", "Bb4/16", "C5/16"
                           ]

hub.speaker.play_notes(ThroughTheFireAndFlames, bpm)
